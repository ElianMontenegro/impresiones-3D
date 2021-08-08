from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
)
from .models import Home
from applications.product.models import Product

class Home(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['product'] = Product.objects.all()


        

        return context
    