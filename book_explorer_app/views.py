from django.http import HttpResponse
import requests
from django.shortcuts import render


def index(request):
    return render(request, "books/index.html")

def search(request, query):
    endpoint = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(endpoint).json()
    total = response.get('totalItems')
    books = response.get('items')
    context = {"query": query, "total": total, "books": books, "number_of_books": len(books)}
    return render(request, "books/search.html", context)

def details(request, query, id):
    endpoint = f'https://www.googleapis.com/books/v1/volumes/{id}'
    response = requests.get(endpoint).json()
    print('response', response)
    title = response.get('volumeInfo').get('title')
    description = response.get('volumeInfo').get('description')
    cover_image_url = response.get('volumeInfo').get('imageLinks').get('smallThumbnail')
    print()
    context = {"title": title, "description": description, "cover_image_url": cover_image_url, "query": query }
    return render(request, "books/details.html", context)