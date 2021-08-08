from django.db import models

from model_utils.models import TimeStampedModel




   
class Home(TimeStampedModel):
    """Model definition for Tag."""

    cover_page = models.URLField("portada")

 

    class Meta:
        verbose_name = 'Home'

    def __str__(self):
        return str(self.id)
