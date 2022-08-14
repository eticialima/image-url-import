from typing import ContextManager, List
from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.views.generic import ListView 
from . import models


class HomeView(ListView): 
    template_name = 'product.html' 
    model = models.Product

    def get_context_data(self, **kwargs): 
        context = super(HomeView, self).get_context_data(**kwargs)    
        context['category'] = models.Category.objects.all() 
        context['products'] = models.Product.objects.all()  
        return context 


class CategoryFilterView(ListView):
    template_name = 'product.html'
    model = models.Product 

    def get_context_data(self, **kwargs):  
        context = super(CategoryFilterView, self).get_context_data(**kwargs)    
        context['category'] = models.Category.objects.all()
        context['products'] = models.Product.objects.filter(category__id=self.kwargs['pk']) 
        return context   

class ProductDetails(DetailView):
    template_name = 'product_details.html'
    model = models.Product  

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['category'] = models.Category.objects.all()
        context['obj'] = models.Product.objects.get(id=self.kwargs['pk']) 
        context['description'] = models.Product.objects.get(id=self.kwargs['pk']).description.replace("\n", "<br>"); 
        return context

 