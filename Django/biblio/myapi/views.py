from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

@api_view(['GET', 'POST', 'DELETE'])
def books_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        book = Book.objects.all()
        
        titre = request.GET.get('titre', None)
        if titre is not None:
            book = book.filter(titre__icontains=titre)
        
        book_serializer = BookSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        Book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=Book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)