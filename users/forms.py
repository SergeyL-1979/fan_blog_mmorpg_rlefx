from django import forms
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm
# from users.models import Account


# ====================  Мой код формы регистрации  ==============================================
class MySignupForm(SignupForm):
    first_name = forms.CharField(max_length=20, label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-label',
                                                               'placeholder': 'Имя', }))
    last_name = forms.CharField(max_length=20, label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-label',
                                                              'placeholder': 'Фамилия', }))

    # birth_date = forms.DateField(label="Дата рождения", initial=datetime.date.today,
    #                              widget=forms.DateInput(attrs={'class': 'form-control',
    #                                                            'id': "example-date-input",
    #                                                            'type': 'date'}))

    def save(self, request):
        user = super(MySignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.is_active = self.cleaned_data['is_active']
        # user.birth_date = self.cleaned_data['birth_date']
        # basic_group = Group.objects.get(name='common')
        # basic_group.user_set.add(user)
        user.is_staff = True
        user.save()
        return user


class MyLoginForm(LoginForm):
    # условие для применения ACCOUNT_FORMS в settings
    """Переопределить форму вхожа allauth"""
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'] = forms.CharField(
            label=("E-MAIL"), widget=forms.TextInput(attrs={'class': 'form-control', }))
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', })


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'is_staff',)
class UserEditForm(forms.ModelForm):
    """Модельная форма редактировать профиль"""

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', ]

        labels = {'username': 'Логин', 'first_name': 'Имя',
                    'last_name': 'Фамилия', 'email': 'email', }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'style': 'width:40ch ',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...',
                'style': 'width:40ch',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...',
                'style': 'width:40ch',
            }),
            'email': forms.EmailInput(attrs={
                'multiple class': 'form-control',
                'style': 'width:40ch',
            }),
        }

    def clean_email(self):
        """Проверка уникальности email"""
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        # Достать всех пользователей с таким email, кроме себя
        if User.objects.filter(email=email).exclude(username=username).exists():
            raise ValidationError('Пользователь с таким email уже зарегистрирован')
        return email
