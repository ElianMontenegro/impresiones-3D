from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
  
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'

    #

    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    email = models.EmailField(
        unique=True,
        error_messages ={ 
            "unique":"El gmail debe ser unico."
        } 
    )
    dni = models.IntegerField("D.N.I")
    user_name = models.CharField('Nombres', max_length=100)
   
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['user_name']

    objects = UserManager()
  
    
    def __str__(self):
        return str(self.id) + ' - ' + self.user_name + ' - ' + self.email

