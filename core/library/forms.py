from django.forms import ModelForm
# from django import forms

from library.models import Book


# class UpdateBookForm(forms.Form):
#     new_description = forms.CharField(
#         max_length = 300,
#         label = 'Краткое описание',
#         help_text='Введите новое описание (максимум 300 символов)',
#         )
class UpdateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_year', 'short_des', 'genre', 'image']
        labels = {
            'title': 'Новое название',
            'author': 'Новый автор',
            'pub_year': 'Новый год публикации', 
            'short_des': 'Новое описание',
            'genre': 'Новый жанр',
            'image': 'Новая обложка',
        }
