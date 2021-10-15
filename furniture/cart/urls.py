from django.urls import path
from . import  views

urlpatterns=[

    # path('add/<int:product_id>/',views.add_cart,name='add'),
    # path('min/<int:product_id>/',views.min,name='min'),
    path('cart/',views.cartview,name='cartview'),
]