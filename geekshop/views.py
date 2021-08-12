from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


main_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'contact', 'name': 'контакты'},
        {'href': 'products:index', 'name': 'продукты'},
]
main_products = [
    {'src': '/img/product-1.jpg', 'h4': 'Отличный стул', 'p': 'Расположитесь комфортно.'},
    {'src': '/img/product-2.jpg', 'h4': 'Стул повышенного качества', 'p': 'Не оторваться.'},
    {'src': '/img/product-3.jpg', 'h4': 'Отличный стул', 'p': 'Расположитесь комфортно.'},
    {'src': '/img/product-4.jpg', 'h4': 'Стул повышенного качества', 'p': 'Не оторваться.'},
]


def main(request):
    title = 'главная'
    main_products_base = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).select_related('user')

    context = {
        'main_menu': main_menu,
        'main_products': main_products_base,
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context=context)


def contact(request):
    title = 'контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).select_related('user')
    context = {
        'main_menu': main_menu,
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context=context)