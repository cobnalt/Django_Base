from django.shortcuts import render
import json
from mainapp.models import ProductCategory

links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'contact', 'name': 'контакты'},
        {'href': 'products:index', 'name': 'продукты'},
]
with open('same_products.json', encoding="utf-8") as json_file:
    same_products = json.load(json_file)


def products(request, pk=None):
    print(pk)
    title = 'каталог/продукты'
    category = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
        'same_products': same_products,
        'category': category,
        'title': title
    }
    return render(request, 'mainapp/products.html', context=context)

