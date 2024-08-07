from django.db import models

from config import settings


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=1000, verbose_name='цена')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='машина', blank=True, null=True,
                            related_name='milage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, verbose_name='мотоцикл', blank=True, null=True,
                             related_name='milage')

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'
        ordering = ('-year', )

