from symtable import Class

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from library.models import Book, Student, StudentBookRelation


# Register your models here.
@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    pass

@admin.register(StudentBookRelation)
class StudentBookAdmim(ModelAdmin):
    pass




