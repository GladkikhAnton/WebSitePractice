from django.shortcuts import render
from products.models import ProductImage, TypeOfProduct

def landing(request):
    return render(request, 'landing/landing.html', locals())

def home(request):
    productsImages = ProductImage.objects.all()
    typeOfProduct = TypeOfProduct.objects.all()
    return render(request, 'landing/home.html', locals())