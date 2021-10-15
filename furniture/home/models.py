from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name="category"
        verbose_name_plural="categories"

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('product_category',args=[self.slug])

class product(models.Model):
    p_name=models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image=models.ImageField(upload_to="product_image")
    stock=models.IntegerField()
    available=models.BooleanField()
    desc=models.CharField(max_length=250)
    price=models.IntegerField()
    material=models.CharField(max_length=250)
    categ=models.ForeignKey(category,on_delete=models.CASCADE)

    class Meta:
        ordering=('p_name',)
        verbose_name="product"
        verbose_name_plural="products"

    def __str__(self):
        return '{}'.format(self.p_name)

    def get_absolute_url(self):
        return reverse('product_details',args=[self.categ.slug,self.slug])