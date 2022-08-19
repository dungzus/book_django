from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Book
from django.template import loader


def index(request):
    return HttpResponse("Hello world")


def getAll(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template_name="book/index.html", context=context)


def getDetail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book isn't exist")
    return render(request=request, template_name="book/detail.html", context={"book": book})
