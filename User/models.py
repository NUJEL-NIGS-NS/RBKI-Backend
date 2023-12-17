from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class MyaccountManager(BaseUserManager):
    def create_user(self,email,user_name,department,password=None,**extrafield):
        
        if not email:
            raise ValueError('Email is Required')
        
        if not user_name:
            raise ValueError('Username is Required')
        
        if not department:
            raise ValueError('department is Required')
        
        user = self.model(
            email =self.normalize_email(email),
            user_name=user_name,
            department = department,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,user_name,department,password=None):
        
        user = self.create_user(
            email =self.normalize_email(email),
            user_name=user_name,
            department = department,
            password=password
             )
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def get_by_natural_key(self, email):
        return self.get(email=email)

        
class User(AbstractBaseUser):
    user_name = models.CharField(_("Username"), max_length=50, unique=True)
    email = models.EmailField(_("user email"), max_length=254, unique=True)
    department = models.CharField(_("department"), max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyaccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "department"]

    def __str__(self):
        return self.user_name
    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return True
    
@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False ,**kwargs):
    if created:
        Token.objects.create(user = instance)