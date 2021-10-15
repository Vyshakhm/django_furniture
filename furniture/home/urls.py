from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('<slug:c_slug>/',views.home,name="product_category"),
    path('<slug:c_slug>/<slug:p_slug>/',views.product_details,name='product_details')

]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)