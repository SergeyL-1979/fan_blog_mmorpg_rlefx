from django.urls import path
from .views import UserEdit
from allauth.account.views import LoginView, SignupForm


urlpatterns = [
    path("login/", LoginView.as_view(), name="account_login"),
    path('signup/', SignupForm, name='signup'),
    path('profile/', UserEdit.as_view(), name='edit_profile'),
    # path('upgrade/', upgrade_me, name='upgrade_me'),
]
