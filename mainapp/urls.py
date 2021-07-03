from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.products, name='products'),
]