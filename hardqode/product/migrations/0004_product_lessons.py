# Generated by Django 4.2.5 on 2023-09-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lessons',
            field=models.ManyToManyField(through='product.ProductLesson', to='product.lesson', verbose_name='Уроки'),
        ),
    ]
