from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, Genre


def index(request):
    """View function for home page of library site"""
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    for genre in Genre.objects.all():
        pass
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    return render(request, 'library/index.html', context=context)

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


class BookListView(generic.ListView):
    """Представление списка книг"""
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    """Представление детальной информации об авторе"""
    model = Book


class AuthorListView(generic.ListView):
    """Представление списка авторов"""
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    """Представление детальной информации о книге"""
    model = Author