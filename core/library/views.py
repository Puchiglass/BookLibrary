from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Book, Author
from .forms import UpdateBookForm


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


def index(request):
    """View function for home page of library site"""
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'library/index.html', context=context)


@login_required
def addbook(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        book = Book()
        book.title = request.POST.get("title")
        book.author_id = request.POST.get("author")
        book.pub_year = request.POST.get("pub_year")
        book.save()
        return HttpResponseRedirect(reverse('succes'))
    # передаем данные в шаблон
    authors = Author.objects.all()
    return render(request, "library/addbook.html", {"authors": authors})

@login_required
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = UpdateBookForm(request.POST)
        if form.is_valid():
            book.short_des = form.cleaned_data['new_description']
            book.save()
            return HttpResponseRedirect(reverse('succes'))
    else:
        proposed_new_description = 'описание осутствует'
        form = UpdateBookForm(initial={'new_description': proposed_new_description}) 
    
    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'library/book_update_des.html', context)

def succes(request):
    return render(request, 'library/succes.html')