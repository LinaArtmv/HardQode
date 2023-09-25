from django.contrib import admin
from .models import Product, Lesson, ProductLesson, Access, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'author')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = ('name', 'url', 'length')


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):

    list_display = ('user', 'product')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('user', 'lesson', 'length', 'status', 'date')


@admin.register(ProductLesson)
class ProductLessonAdmin(admin.ModelAdmin):

    list_display = ('product', 'lesson')
