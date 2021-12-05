from urllib import response

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count,Max,Min,Sum,Avg

from store.models import Product, OrderItem, Order


# Create your views here.
def sayHello(request):
    # __gt=>
    # __gte= >=
    # __lt= <
    # __lte= <=
    # __range=(20,30) = between20 and 30
    # __contains == Uppercase sensitive words
    # __icontains == Non sensitive words same for __startswith and __endswith

    # queryset = Product.objects.filter(unit_price__range=(20,30))

    # Products: inventory<10 and price<20
    # queryset = Product.objects.filter(inventory__lt=10 ,unit_price__lt=20)
    # queryset = Product.objects\
    #     .filter(inventory__lt=10)\
    #     .filter(unit_price__lt=20)

    # Products: inventory<10 OR !price<20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) | ~Q(unit_price__lt=20))

    # Products: inventory<10 OR price<20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10)|Q(unit_price__lt=20))

    # where inventory==unit_price
    # queryset = Product.objects.filter(inventory=F('unit_price'))

    # order_by asc title
    # queryset = Product.objects.order_by('title')
    # OR
    #  queryset = Product.objects.order_by('-title').reverse()

    # order_by desc title desc
    # queryset = Product.objects.order_by('-title')

    # product = Product.objects.order_by('unit_price')[0]
    # show first 5 of aray
    # queryset = Product.objects.all()[:5]

    # queryset = Product.objects.values('id','title','collection__title')
    # select_related if its one to many
    # prefetch_related if its many to many
    # queryset = Product.objects.select_related('collection').all()

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by(
    #     '-placed_at')[:5]

    result = Product.objects.aggregate(count=Count('id'),min_price=Min('unit_price'))

    return render(request, "hello.html", {"name": "Pavel", 'result': result})

    # find products that are ordered and sort them by title
    # queryset=Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
