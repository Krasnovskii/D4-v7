from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import path
from .models import Book
from django.template import loader
from p_library.models import Redaction

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data))


def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    data = {
        "redactions": redactions,
    }
    return HttpResponse(template.render(data, request))

