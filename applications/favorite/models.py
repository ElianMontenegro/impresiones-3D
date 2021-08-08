from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from applications.product.models import Product

# Create your models here.

class Favorite(TimeStampedModel):
    """Model definition for Favorite."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )


    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return str(self.id) +  '- ' + self.product.name
