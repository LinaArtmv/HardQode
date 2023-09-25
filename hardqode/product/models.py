from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Lesson(models.Model):
    """Модель урока."""

    name = models.CharField('Название урока',
                            max_length=100)
    url = models.URLField('Ссылка на видео',
                          unique=True)
    length = models.PositiveSmallIntegerField('Длина видео в секундах')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """Модель продукта."""

    name = models.CharField('Название продукта',
                            max_length=100)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='products',
                               verbose_name='Автор')
    lessons = models.ManyToManyField(Lesson,
                                     through='ProductLesson',
                                     verbose_name='Уроки')

    def __str__(self) -> str:
        return self.name


class Access(models.Model):
    """Модель для управления доступом пользователей к продуктам."""

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='access')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='access')


class Review(models.Model):
    """Модель оценки просмотров уроков пользователями."""

    STATUS_CHOICES = (
        ('Просмотрено', 'Просмотрено'),
        ('Не просмотрено', 'Не просмотрено'))

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='reviews')
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    length = models.PositiveSmallIntegerField('Просмотр в секундах')
    status = models.CharField('Статус',
                              max_length=15,
                              choices=STATUS_CHOICES,
                              default='Не просмотрено')
    date = models.DateField(auto_now=True)


class ProductLesson(models.Model):
    """Модель для связи уроков и продуктов."""

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product_lesson')
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               related_name='product_lesson')
