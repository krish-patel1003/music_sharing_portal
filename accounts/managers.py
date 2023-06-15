from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    '''
    Object Manager class for AUTH_USER_MODEL.
    '''
    

    def create_user(self, email, first_name, last_name, password=None, **kwargs):
        '''
        create_user method is executed everytime an object of User class is created.
        '''

        if first_name is None:
            raise TypeError('first_name not provided')
        
        if last_name is None:
            raise TypeError('last_name not provided')
        
        if email is None:
            raise TypeError('email not provided')
        
        email = self.normalize_email(email)

        user = self.model(
            email = email, first_name=first_name, last_name=last_name, **kwargs)

        user.set_password(password)
        user.save()

        return user
    

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        '''
        create_superuser method is executed everytime a super user has to be created.
        '''

        if first_name is None:
            raise TypeError('first_name not provided')
        
        if last_name is None:
            raise TypeError('last_name not provided')
        
        if email is None:
            raise TypeError('email not provided')
        
        if password is None:
            raise TypeError('password not provided')
        
        email = self.normalize_email(email)
        user = self.create_user(
            first_name=first_name, last_name=last_name, email=email, password=password, **kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
