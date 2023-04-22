from django.db import models
from book.models import Book
from user.models import User

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'{self.user}, {self.book}, {self.date}'

    class Meta:
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупки'