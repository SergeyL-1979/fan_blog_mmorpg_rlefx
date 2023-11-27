# from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.models import User
# from django.urls import reverse
#
#
# class MyAccountManager(BaseUserManager):
#     models = User
#
#     def create_user(self, email, username, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')
#
#         user = self.model(email=self.normalize_email(email), username=username, )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(email, password=password, )
#         user.staff = True
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#     def get_absolute_url(self):
#         return reverse('edit', kwargs={"pk": self.pk})
#     # def get_absolute_url(self):
#     #     return f'/profile/{self.pk}'