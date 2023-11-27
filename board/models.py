from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """ Модель Category(КАТЕГОРИЯ) связующая модель CategorySubscribers(ПОДПИСЧИКОВ НА КАТЕГОРИЮ) """
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = slugify(str(self.name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Получить ссылку на объект"""
        return reverse('category', kwargs={'pk': self.pk})


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = RichTextField(blank=True, null=True, verbose_name='Описание')
    # response = models.ForeignKey('Response', models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        """ Строковое отображение объекта """
        return f'{self.title}'

    def get_absolute_url(self):
        """ Получить ссылку на объект """
        return reverse('ads_detail', kwargs={'pk': self.pk})


class Response(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    # responded_user = models.ManyToManyField(CustomUser, related_name='post_responses')
    accepted_responses = models.ManyToManyField(User, related_name='ads_accepted_responses', )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class PrivatePage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, models.CASCADE)

    class Meta:
        verbose_name = 'Приват'
        verbose_name_plural = 'Приват'
