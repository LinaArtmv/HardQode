# Generated by Django 4.2.5 on 2023-09-25 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название урока')),
                ('url', models.URLField(unique=True, verbose_name='Ссылка на видео')),
                ('length', models.PositiveSmallIntegerField(verbose_name='Длина видео в секундах')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Продукты')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.PositiveSmallIntegerField(verbose_name='Просмотр в секундах')),
                ('status', models.CharField(choices=[('Просмотрено', 'Просмотрено'), ('Не просмотрено', 'Не просмотрено')], default='Не просмотрено', max_length=15, verbose_name='Статус')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_lesson', to='product.lesson')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_lesson', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
