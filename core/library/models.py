from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Model representing a author."""

    first_name = models.CharField(
        max_length=100,
        default='',
        help_text='имя')
    last_name = models.CharField(
        max_length=100,
        default='',
        help_text='фамилия')
    surename = models.CharField(
        max_length=100,
        default='', 
        null=True, 
        blank=True, 
        help_text='отчество, если есть')
    birth_day = models.DateField(blank=True, help_text='1900-01-01')
    short_bio = models.CharField(
        max_length=300, 
        blank=True,  
        help_text='биография', 
        verbose_name='short biography'
        )
    portrait = models.ImageField(
        upload_to='images/authors',
        blank=True, 
        help_text='портрет', 
        verbose_name='portrait',
        )
    
    def get_name(self):
        """Возвращает полное имя"""
        if self.surename:
            return f'{self.first_name} {self.surename} {self.last_name}'
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к подробной записи этого автора."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text = 'жанр')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """Model representing a book."""

    title = models.CharField(max_length=200, help_text='title')
    author = models.ForeignKey(
        Author, 
        null=True,
        on_delete=models.SET_NULL, 
        help_text='автор'
        )
    pub_year = models.IntegerField(
        default=0, 
        blank=True, 
        help_text='год публикации', 
        verbose_name='year of published'
        )
    short_des = models.CharField(
        max_length=300, 
        blank=True, 
        help_text='описание', 
        verbose_name='short description'
        )
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.SET_NULL, 
        null=True, 
        help_text = 'жанр'
        )
    image = models.ImageField(
        upload_to='images/book',
        blank=True, 
        help_text='обложка', 
        verbose_name='cover image',
        )
    
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к подробной записи этой книги."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    """Model representing a comment"""

    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    name = models.CharField(max_length=250)
    date_pub = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к подробной записи этой книги."""
        return reverse('books')

    def __str__(self) -> str:
        return f'Book: {self.book.title}, name: {self.name}'