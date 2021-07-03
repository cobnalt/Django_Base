from django.shortcuts import render
import json

links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'contact', 'name': 'контакты'},
        {'href': 'products', 'name': 'продукты'},
]
with open('same_products.json', encoding="utf-8") as json_file:
    same_products = json.load(json_file)


def products(request):
    title = 'каталог/продукты'
    context = {
        'links_menu': links_menu,
        'same_products': same_products,
        'title': title
    }
    return render(request, 'mainapp/products.html', context=context)

