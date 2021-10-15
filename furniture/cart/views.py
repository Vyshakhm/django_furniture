from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.core.exceptions import ObjectDoesNotExist
from home.models import *
from django.contrib.auth.models import auth,User

# Create your views here.

def cartview(request,tot=0,count=0,cart_item=None):

    ct_id=request.session.session_key
    print(ct_id)
    print(request.session.get('user'))
    return render(request,'cart.html')




def add_cart(request,product_id):

    prodt=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cartid=c_id(request))
        ct.save()
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cartid=c_id(request))
        ct.save()
    try:
        ct_item=item.objects.get(prod=prodt,cart=ct)
        if ct_item.quantity < ct_item.prod.stock:
            ct_item.quantity+=1
        ct_item.save()
    except item.DoesNotExist:
        ct_item=item.objects.create(prod=prodt,cart=ct,quantity=1)
        ct_item.save()
    return redirect('cartview')
