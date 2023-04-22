from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    author = models.CharField(max_length=100, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Рік')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return f'{self.title}, {self.author}, {self.year}, {self.price}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'