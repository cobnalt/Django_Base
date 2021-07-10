import random

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product

main_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'contact', 'name': 'контакты'},
        {'href': 'products:index', 'name': 'продукты'},
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True, category__is_active=True)

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def products(request, pk=None, page=1):

    title = 'каталог/продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True,
                                              category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'main_menu': main_menu,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'title': title,
        }
        return render(request, 'mainapp/products_list.html', context=context)

    context = {
        'main_menu': main_menu,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'title': title,
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'main_menu': main_menu,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', content)