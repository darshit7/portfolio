'''
Models for user_management application will be defined here.
'''

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    '''
    Query manager class for User model.
    '''
    def create_user(self, username, email, full_name, password=None):
        if not username:
            raise ValueError(_('User must have username.'))
        if not email:
            raise ValueError(_('User must have email address.'))
        if not full_name:
            raise ValueError(_('User must have full name.'))
        user = self.model(username=username, email=email, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, password=None):
        '''
        Method to create super user of system.
        '''
        user = self.create_user(username, email, full_name, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    '''
    User model class contains information of all users.
    '''
    username = models.CharField(_('Username'), max_length=40, blank=False,
            null=False, unique=True)
    '''
    This field defines username. It must be unique and maximum 40 Characters
    are allowed.
    '''

    full_name = models.CharField(_('Full Name'), max_length=80, blank=False,
            null=False)
    '''
    This field defines full name of user.
    '''

    email = models.EmailField('Email', unique=True)
    '''
    This field stores email address of user.
    '''

    is_staff = models.BooleanField(_('Is Staff Member'), default=True)
    '''
    This flag defines if user is staf user or not.
    '''

    is_deleted = models.BooleanField(_('Is Deleted'), default=False)
    '''
    This flag defines if user is deleted or not.
    '''

    is_active = models.BooleanField(_('Is Active'), default=True)
    '''
    This field defines status of user. It is True if user active otherwise
    False.
    '''

    is_admin = models.BooleanField(_('Is Admin'), default=False)
    '''
    This falg defines if user is admin or not.
    '''

    created_at = models.DateTimeField(auto_now_add=True)
    '''
    This field stores date of user creation.
    '''

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['full_name', 'email', ]

    objects = UserManager()

    def __str__(self):
        '''
        This method defines human readable representation of User object.
        Here it returns full name.
        '''
        return self.full_name

    def has_perm(self, perm, obj=None):
       return True

    def has_module_perms(self, app_label):
        return True
    def get_short_name(self):
        return self.full_name

    class Meta:
        '''
        This class defines meta information of User model.
        '''
        db_table = 'um_user'
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['full_name',]

