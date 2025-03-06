from datetime import date, timedelta

from django.db import models



class Student(models.Model):
    first_name = models.CharField("Имя",max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    group_number = models.PositiveSmallIntegerField("Номер группы", default=0)
    #books = models.ManyToManyField( Book, through= 'StudentBookRelation', related_name='books')

    def __str__(self):
        return f'Id {self.id} : {self.first_name}" "{self.last_name} '


class Book(models.Model):
    name = models.CharField("Название", max_length=255)
    author = models.CharField("Автор", max_length=255)
    edition_number = models.PositiveSmallIntegerField("Номер издания", default=1)
    number_pages = models.PositiveSmallIntegerField("Кол Страниц", default=1)
    books_in_stock = models.PositiveSmallIntegerField("Количество книг", default= 0)
    availible_books = models.PositiveSmallIntegerField("Books available", default= 0)
    reader = models.ManyToManyField(Student, through= 'StudentBookRelation', related_name='reader')

    def __str__(self):
        return f'Id {self.id} : {self.name}'

class StudentBookRelation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    reader = models.ForeignKey(Student, on_delete=models.PROTECT)
    book_returned = models.BooleanField(default= False)
    receiving_date = models.DateField(default= date.today())
    return_deadline =  models.DateField(default= date.today()+ timedelta(days = 30))

    def __str__(self):
        return f'{self.reader.first_name}" "{self.reader.last_name} : {self.book.name} :returned {self.book_returned}'
