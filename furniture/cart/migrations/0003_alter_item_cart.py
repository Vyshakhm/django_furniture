# Generated by Django 3.2.7 on 2021-09-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_categ_item_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist'),
        ),
    ]
