# Generated by Django 4.2.5 on 2023-09-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]