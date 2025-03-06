"""
URL configuration for University_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from library.views import BookDetail, BookList, home, BookCreate, book_delete, StudentsList, StudentDetail, \
    StudentCreate, student_delete, OnHandBook, GiveBook, ReaderBookRelationCreate, book_return

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('book/<int:pk>/', BookDetail.as_view(), name = 'book-detail'),
    path('book/new/', BookCreate.as_view(), name = 'book-new'),
    path('book/', BookList.as_view(), name = 'book-list'),
    path(r'^book_delete/<int:pk>', book_delete, name='bookdelete-view'),

    path('student/', StudentsList.as_view(), name = 'student-list'),
    path('student/<int:pk>/', StudentDetail.as_view(), name = 'student-detail'),
    path('student/new/', StudentCreate.as_view(), name = 'student-new'),
    path(r'^student_delete/<int:pk>', student_delete, name='student_delete-view'),
    path(r'^student_book_on_hand/<int:pk>', OnHandBook.as_view(), name='book_onHand-view'),
    path(r'^student_givebook/<int:pk>', GiveBook.as_view(), name='givebook-view'),
    path('relation/<int:book_id>/<int:reader_id>/', ReaderBookRelationCreate.as_view(), name = 'relation-create'),
    path('book_return/<int:pk> ', book_return , name = 'book-return'),

]

