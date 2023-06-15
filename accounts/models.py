from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom AUTH_USER_MODEL.
    '''
    email = models.EmailField(max_length=255, unique=True, null=False, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        '''
        returns a string - "<email>".
        '''
        
        return self.email
    
    def get_full_name(self):
        '''
        returns a string - "<first_name> <last_name>".
        '''
        
        return f'{self.first_name} {self.last_name}'
    
    def tokens(self):
        '''
        returns a object - containing refresh_token and access_token.
        '''

        refresh_token = RefreshToken.for_user(self)
        return {
            'refresh_token':str(refresh_token),
            'access_token':str(refresh_token.access_token)
        }


