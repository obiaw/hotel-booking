from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField


class Hotel(models.Model):
    name = models.CharField("Hotel Name", max_length=100)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name


class Rooms(models.Model):
    room_type = models.CharField(max_length=100)
    price = MoneyField(max_digits=65, decimal_places=2, default_currency='USD')
    number_available = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.room_type

