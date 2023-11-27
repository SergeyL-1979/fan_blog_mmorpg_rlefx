"""
Django settings for mmorpg_project project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = bool(int(os.environ.get('DEBUG', default=1)))

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # === django-allauth ===
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ========================
    # === django-ckeditor ====
    'ckeditor',
    'ckeditor_uploader',
    # =========================
    # ===== Фильтры django-filter ====
    'django_filters',
    # ===== My Apps =====
    'users.apps.UsersConfig',
    'board.apps.BoardConfig',
    # ====================
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # ========= Add the account middleware =========
    "allauth.account.middleware.AccountMiddleware",
    # ==============================================
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mmorpg_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mmorpg_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# =========================================================================================

# ============== USER SETTINGS =================================================
CKEDITOR_UPLOAD_PATH = "uploads/"
SITE_ID = 1

# AUTH_USER_MODEL = 'users.User'
# AUTH_USER_MODEL = 'users.CustomUser'
# ============== Основные настройки allauth ===========================
LOGIN_REDIRECT_URL = '/account/profile/'
# LOGIN_URL = '/account/login/'
LOGIN_URL = 'account/login/'
# LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
)

""" The user is required to hand over an e-mail address when signing up. """
ACCOUNT_EMAIL_REQUIRED = True

""" Enforce uniqueness of e-mail addresses. The emailaddress.email model field is set to UNIQUE.
 Forms prevent a user from registering with or adding an additional email address if 
 that email address is in use by another account. """
ACCOUNT_UNIQUE_EMAIL = True

""" The user is required to enter a username when signing up.
 Note that the user will be asked to do so even if ACCOUNT_AUTHENTICATION_METHOD is set to email. 
 Set to False when you do not wish to prompt the user to enter a username. """
ACCOUNT_USERNAME_REQUIRED = False

""" (=”username” | “email” | “username_email”)
    Specifies the login method to use – whether the user logs in by entering their username, 
    e-mail address, or either one of both. Setting this to “email” requires ACCOUNT_EMAIL_REQUIRED=True """
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'

""" Determines the e-mail verification method during signup – choose one of "mandatory", "optional", or "none". """
ACCOUNT_EMAIL_VERIFICATION = True
# ACCOUNT_EMAIL_VERIFICATION = 'optional'

# ACCOUNT_FORMS = {'signup': 'accounts.forms.MyCustomSignupForm'}
ACCOUNT_FORMS = {
    'login': 'users.forms.MyLoginForm',
    'signup': 'users.forms.MySignupForm',
    # 'change_password': 'users.forms.MyChangePasswordForm',
    # 'reset_password': 'users.forms.MyResetPasswordForm',
}

# Указываем файл, где храниться функция переопределения редиректов allauth
# ACCOUNT_ADAPTER = 'users.adapter.MyAccountAdapter'

# SOCIALACCOUNT_FORMS = {'signup': 'accounts.forms.MyCustomSocialSignupForm'}












# ============= Настройки электронной почты =========
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST = os.environ.get('HOST_SMTP_YA')
EMAIL_PORT = os.environ.get('PORT_SMTP')
EMAIL_HOST_USER = os.environ.get('HOST_USER_YA')  # ваш QQ Номер счета и код авторизации
EMAIL_HOST_PASSWORD = os.environ.get('YANDEX_ID')
EMAIL_USE_TLS = True  # Здесь должно быть True, Иначе отправка не удалась
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = [('Dos', 'dos891@mail.ru'),]
EMAIL_SUBJECT_PREFIX = '[FanBlog] '
# =====================================================



