from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .models import Book, Author
from .forms import UpdateBookForm


class BookListView(generic.ListView):
    """Представление списка книг"""
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    """Представление детальной информации об авторе"""
    model = Book

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'pub_year', 'short_des', 'genre', 'image']

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'pub_year', 'short_des', 'genre', 'image']
    
class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')

class AuthorListView(generic.ListView):
    """Представление списка авторов"""
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    """Представление детальной информации о книге"""
    model = Author

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'surename', 'birth_day', 
              'short_bio', 'portrait']
    
class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'surename', 'birth_day', 
              'short_bio', 'portrait']
    
class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


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


def succes(request):
    return render(request, 'library/succes.html')


# Мои старые функции добавления и обновления книги
# 
# @login_required
# def addbook(request):
#     # если запрос POST, сохраняем данные
#     if request.method == "POST":
#         book = Book()
#         book.title = request.POST.get("title")
#         book.author_id = request.POST.get("author")
#         book.pub_year = request.POST.get("pub_year")
#         book.save()
#         return HttpResponseRedirect(reverse('succes'))
#     # передаем данные в шаблон
#     authors = Author.objects.all()
#     return render(request, "library/addbook.html", {"authors": authors})

# @login_required
# def update_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = UpdateBookForm(request.POST, request.FILES or None, instance=book)
#         if form.is_valid():
#             book.title = form.cleaned_data['title']
#             book.author = form.cleaned_data['author']
#             book.pub_year = form.cleaned_data['pub_year']
#             book.short_des = form.cleaned_data['short_des']
#             book.image = form.cleaned_data['image']
#             #book.short_des = form.cleaned_data['new_description']
#             book.save()
#             return HttpResponseRedirect(reverse('succes'))
#     else:
#         form = UpdateBookForm(instance=book) 
    
#     context = {
#         'form': form,
#         'book': book,
#     }

#     return render(request, 'library/book_update_des.html', context)