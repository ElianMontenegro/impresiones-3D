from datetime import timedelta,datetime

from django.db import models
from model_utils.models import TimeStampedModel

from django.template.defaultfilters import slugify


        
class Colors(models.Model):
    """ Representa color de un producto """

    color = models.CharField(
        'color', 
        max_length=30, 
        unique=True
    )
    
    class Meta:
        verbose_name = 'Color Producto'
        verbose_name_plural = 'Colores'

    def __str__(self):
        return str(self.id) + ' - ' + (self.color)



class Product(TimeStampedModel):
    name = models.CharField(
        'Nombre del producto', 
        max_length=50
    )
    description = models.TextField(
        'Descripcion del producto',
        blank=True,
    )
    stock = models.PositiveIntegerField(
        'Cantidad en almacen',
        default=0
    )
    price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    image_main = models.URLField(blank=True)
    image = models.URLField(blank=True)
    color = models.ManyToManyField(Colors)
    anulate = models.BooleanField(
        'Eliminado',
        default=False
    )
    offer = models.BooleanField(
        'En oferta',
        default=False,
        blank=True,
    )
    discount = models.PositiveIntegerField(
        'Descuento',
        default=0,
        blank=True,
    )
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return str(self.id) + '-' + self.name

    def save(self, *args ,**kwargs,):
        
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second,
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.name, str(seconds))
        self.slug = slugify(slug_unique)

    
class Category(TimeStampedModel):
    """Model definition for Category."""

    name = models.CharField(
        'nombre', 
        max_length=30,
        unique = True
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
    )

    class Meta:

        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


