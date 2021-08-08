from django import forms

from .models import Product 


class FormProduct(forms.ModelForm):
    """FormProduct definition."""
    class Meta:
        model = Product
    
        fields=(
            '__all__'
        )
       
    # validations
    