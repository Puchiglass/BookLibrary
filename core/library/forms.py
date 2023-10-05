from django import forms


class UpdateBookForm(forms.Form):
    new_description = forms.CharField(
        max_length = 300,
        label = 'Краткое описание',
        help_text='Введите новое описание (максимум 300 символов)',
        )