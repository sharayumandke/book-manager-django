from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
import requests  # 👈 for external API calls


# 🌐 Home view (for rendering index.html)
def home(request):
    return render(request, 'index.html')


# 📚 Existing CRUD views
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('id')  # sorted by ID
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 🔄 Import book using Open Library API
@api_view(['POST'])
def import_book(request):
    title = request.data.get('title')
    if not title:
        return Response({"error": "Please provide a book title"}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch from Open Library API
    response = requests.get(f'https://openlibrary.org/search.json?title={title}')
    data = response.json()

    if data['num_found'] == 0:
        return Response({"error": "No books found with that title"}, status=status.HTTP_404_NOT_FOUND)

    # Take the first result
    book_data = data['docs'][0]
    new_book = {
        "title": book_data.get('title', 'Unknown Title'),
        "author": book_data.get('author_name', ['Unknown Author'])[0],
        "published_date": "2025-10-21",  # Default or current date
        "price": 100  # Temporary default
    }

    serializer = BookSerializer(data=new_book)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
