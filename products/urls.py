from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  
    path("product-detail/<int:pk>/", views.ProductDetails.as_view(), name="product-detail"),   
    path("category/<int:pk>/", views.CategoryFilterView.as_view(), name="category"),  
]