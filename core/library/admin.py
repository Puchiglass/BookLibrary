from django.contrib import admin

from .models import Author, Genre, Book, Comment


class BookInline(admin.TabularInline):
    model = Book
    fields = ['title', 'pub_year', 'short_des']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'surename', 'birth_day')
    fields = [('first_name', 'last_name', 'surename'),'birth_day', 'short_bio', 'portrait']
    inlines = [BookInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'pub_year')
    list_filter = ['author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'book')
    list_filter = ['name', 'date_pub']
    fields = [('name', 'book'), 'content']