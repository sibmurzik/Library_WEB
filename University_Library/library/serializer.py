from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from library.models import Book, Student, StudentBookRelation


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields ="__all__"


class StudentSerializer(ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    annotated_booksOnHand = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        #fields ="__all__"
        fields = ('id', 'first_name', 'last_name', 'group_number', 'annotated_booksOnHand' )

class StudentBookRelationSerializer(ModelSerializer):
    class Meta:
        model = StudentBookRelation
        fields = "__all__"

