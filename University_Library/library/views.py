from django.db.models import Count, Case, When
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from library.models import Book, Student, StudentBookRelation
from library.serializer import BookSerializer, StudentSerializer, StudentBookRelationSerializer


# Create your views here.
#Getting of book's list
class BookList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_list.html'

    def get(self, request):
        queryset = Book.objects.all().order_by('id')
        return Response({'books': queryset})


class BookDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='book_edit.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response({'serializer': serializer, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'book': book})
        serializer.save()
        return redirect('book-list')


class BookCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='book_edit.html'

    def get(self, request):
        book = Book.objects.create()
        serializer = BookSerializer(book)
        return Response({'serializer': serializer, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'book': book})
        serializer.save()
        return redirect('book-list')



def book_delete(request, pk):
    object =  Book.objects.get(id=pk)
    object.delete()
    return redirect('book-list')


class StudentsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'students_list.html'

    def get(self, request):
        queryset = (Student.objects.all().annotate(
            annotated_booksOnHand=Count(Case(When(studentbookrelation__book_returned=False, then=1))))
                    .order_by('id'))


        return Response({'students': queryset})

class StudentDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='student_edit.html'

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response({'serializer': serializer, 'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Student , pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'student': student})
        serializer.save()
        return redirect('student-list')


class StudentCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='student_edit.html'

    def get(self, request):
        student = Student.objects.create()
        serializer = StudentSerializer(student)
        return Response({'serializer': serializer, 'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Book, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'student': student})
        serializer.save()
        return redirect('student-list')



def student_delete(request, pk):
    object =  Student.objects.get(id=pk)
    object.delete()
    return redirect('student-list')

class OnHandBook(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_on_hand.html'

    def get(self, request, pk):
        reader = Student.objects.get(id =pk)
        queryset = StudentBookRelation.objects.all().filter(reader = reader).order_by('id')
        return Response({'books': queryset})


class GiveBook(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_distibute.html'

    def get(self, request, pk):
        reader = Student.objects.get(id =pk)
        queryset = Book.objects.all().order_by('id')
        return Response({'books': queryset, 'reader': reader})

class ReaderBookRelationCreate(APIView):

    def get(self, request, book_id, reader_id):
        book = Book.objects.get(id = book_id)
        reader = Student.objects.get(id = reader_id)
        book_reader_relation = StudentBookRelation.objects.create(book = book, reader = reader)
        serializer = StudentBookRelationSerializer(book_reader_relation)
        return redirect('student-list')


def book_return(request, pk):
    object =  StudentBookRelation.objects.get(id=pk)
    object.delete()
    return redirect('student-list')



def home(request):
    return render(request, 'base.html')

