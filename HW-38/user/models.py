from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    age = models.IntegerField(verbose_name='Вік')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}'

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
