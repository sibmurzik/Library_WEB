from django.db import models

# Create your models here.
#Таблица книг
class Book(models.Model):
    name = models.CharField("Название", max_length=255)
    author = models.CharField("Автор", max_length=255)
    edition_number = models.PositiveSmallIntegerField("Номер издания", default=1)
    number_pages = models.PositiveSmallIntegerField("Кол Страниц")
    books_in_stock = models.PositiveSmallIntegerField("Количество книг", default= 0)


class Student(models.Model):
    first_name = models.CharField("Имя",max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    group_number = models.PositiveSmallIntegerField("Номер группы")

