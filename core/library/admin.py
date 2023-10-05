from django.contrib import admin

from .models import Author, Genre, Book


class BookInline(admin.TabularInline):
    model = Book
    fields = ['title', 'pub_year', 'short_des']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surename', 'birth_day')
    fields = [('first_name', 'last_name', 'surename'),'birth_day', 'short_bio', 'portrait']
    inlines = [BookInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'pub_year')