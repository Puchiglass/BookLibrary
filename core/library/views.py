from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Book, Author


def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

def addbook(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        book = Book()
        book.title = request.POST.get("title")
        book.author_id = request.POST.get("author")
        book.pub_year = request.POST.get("pub_year")
        book.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    authors = Author.objects.all()
    return render(request, "library/addbook.html", {"authors": authors})