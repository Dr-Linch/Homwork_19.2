from django.shortcuts import render
from catalog.models import Product, Category
from django.shortcuts import get_object_or_404


def index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contact.html')


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/product.html', context)
