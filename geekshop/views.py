from django.shortcuts import render


links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'contact', 'name': 'контакты'},
        {'href': 'products', 'name': 'продукты'},
]
main_products = [
    {'src': '/img/product-1.jpg', 'h4': 'Отличный стул', 'p': 'Расположитесь комфортно.'},
    {'src': '/img/product-2.jpg', 'h4': 'Стул повышенного качества', 'p': 'Не оторваться.'},
    {'src': '/img/product-3.jpg', 'h4': 'Отличный стул', 'p': 'Расположитесь комфортно.'},
    {'src': '/img/product-4.jpg', 'h4': 'Стул повышенного качества', 'p': 'Не оторваться.'},
]



def main(request):
    title = 'главная'
    context = {
        'links_menu': links_menu,
        'main_products': main_products,
        'title': title,
    }
    return render(request, 'geekshop/index.html', context=context)


def contact(request):
    title = 'контакты'
    context = {
        'links_menu': links_menu,
        'main_products': main_products,
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context=context)