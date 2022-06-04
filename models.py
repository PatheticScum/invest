from operator import mod
from django.db import models
from distutils.command.upload import upload
from turtle import title
from django.contrib.auth import admin
from django.db import models
from django.urls import reverse


# Create your models here.

class Addproject(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(upload_to='image/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    regions = models.ForeignKey('Region', on_delete=models.SET_NULL, verbose_name="Регион", null=True)
    prices = models.ForeignKey('Price', on_delete=models.SET_NULL, verbose_name="Цена", null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name="Категория", null=True)


def __str__(self):
    return self.title


class Partner(models.Model):
    photo = models.ImageField(upload_to='image/', blank=True)

    def __str__(self):
        return self.photo


class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Region(models.Model):
    name = models.CharField("Регион", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Price(models.Model):
    name = models.CharField("Цена", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
