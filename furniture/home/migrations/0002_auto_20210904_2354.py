# Generated by Django 3.2.7 on 2021-09-04 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('image', models.ImageField(upload_to='product_image')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField()),
                ('desc', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('material', models.CharField(max_length=250, unique=True)),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('p_name',),
            },
        ),
    ]