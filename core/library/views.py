from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .forms import RegisterUserForm

from .models import Book, Author


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

def register_request(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return HttpResponseRedirect(reverse('succes'))
        else: # просто вывод красного сообщения будет(см. в register.html)
            form = RegisterUserForm()
            context = {'register_form': form, 'error': True}
            return render(request,
                          template_name='registration/register.html',
                          context=context)
    form = RegisterUserForm()
    context = {'register_form': form,}
    return render(request, template_name='registration/register.html', context=context)