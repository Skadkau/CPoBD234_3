from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from anketa.models import Naviki, Sertifikat


# Create your models here.


class Otvet(models.Model):
    polzovatel = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    navik = models.ForeignKey(Naviki, on_delete=models.PROTECT, verbose_name="Навык")
    ball = models.IntegerField(verbose_name="Баллы")
    data = models.DateTimeField(verbose_name="Дата")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Ответ"
        verbose_name_plural = "Ответ"

    def __str__(self):
        return self.polzovatel

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Otvet._meta.fields]


class Sertif(models.Model):
    sertif = models.ForeignKey(Sertifikat, on_delete=models.PROTECT, verbose_name="Сертификат")
    polzovatel = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    osnnavik = models.IntegerField(verbose_name="Основной навык")
    vsenavik = models.IntegerField(verbose_name="Все навыки")
    data = models.DateTimeField(verbose_name="Дата")
    itog = models.FileField(max_length=255, verbose_name="Сертификат")

    class Meta:
        ordering = ["-polzovatel"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.itog

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Sertif._meta.fields]