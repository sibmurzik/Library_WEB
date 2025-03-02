from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Student
from library.serializer import BookSerializer, StudentSerializer


# Create your views here.
#Представление книг
class BookViewDetail(APIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#Представление студентов
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
