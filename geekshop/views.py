from django.shortcuts import render


def main(request):
    return render(request, 'geekshop/index.html')


def contact(request):
    return render(request, 'geekshop/contact.html')