# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
#
# from users.managers import MyAccountManager
#
#
# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=50, verbose_name='first_name')
#     last_name = models.CharField(max_length=50, verbose_name='last_name')
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     objects = MyAccountManager()
#
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __str__(self):
#         return self.email
#
#     # Для проверки разрешений. для простоты у всех администраторов есть ВСЕ разрешения
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_perms(self, perm_list, obj=None):
#         """
#         Returns True if the user has each of the specified permissions. If
#         object is passed, it checks if the user has all required perms for this
#         object.
#         """
#         for perm in perm_list:
#             if not self.has_perm(perm, obj):
#                 return False
#         return True
#
#     # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
#     def has_module_perms(self, app_label):
#         return True
#         # return self.is_admin
#         # return self.is_superuser
#
#     # class Meta:
#     #     db_table = 'auth_user'
#
# # ==============================================================
