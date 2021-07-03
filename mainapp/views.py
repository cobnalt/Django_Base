from django.shortcuts import render
import json
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404

main_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'contact', 'name': 'контакты'},
        {'href': 'products:index', 'name': 'продукты'},
]
with open('same_products.json', encoding="utf-8") as json_file:
    same_products = json.load(json_file)


def products(request, pk=None):

    title = 'каталог/продукты'
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'main_menu': main_menu,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'title': title,
            'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', context=context)

    context = {
        'main_menu': main_menu,
        'links_menu': links_menu,
        'same_products': same_products,
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=context)
