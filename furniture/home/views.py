from django.shortcuts import render,get_object_or_404,redirect
from.models import *
from django.db.models import Q

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prod=product.objects.filter(categ=c_page)
    else:
        prod=product.objects.all()
    cat=category.objects.all()
    return render(request,'index.html',{'ct':cat,'prod':prod})


def product_details(request,c_slug,p_slug):
    try:
        prod=product.objects.get(categ__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    cat = category.objects.all()
    return render(request,'single-product.html',{'prod':prod,'ct':cat})

def search(request):
    prod=None
    query=None
    if 'search' in request.GET:
        query=request.GET.get('search')
        prod=product.objects.all().filter(Q(p_name__contains=query)|Q(desc__contains=query))
    else:
        redirect('/')
    cat=category.objects.all()
    return render(request,'search.html',{'pro':prod,'ct':cat})