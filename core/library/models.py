from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Model representing a author."""
    name = models.CharField(max_length=200, help_text='name')
    birth_day = models.DateField(blank=True, help_text='1900-01-01')
    short_bio = models.CharField(
        max_length=300, 
        blank=True,  
        help_text='biography', 
        verbose_name='short biography'
        )

    def get_absolute_url(self):
            """Возвращает URL-адрес для доступа к подробной записи этого автора."""
            return reverse('author-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text = 'book genre')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """Model representing a book."""
    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)

    title = models.CharField(max_length=200, help_text='title')
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        help_text='author'
        )
    pub_year = models.IntegerField(
        default=0, 
        blank=True, 
        help_text='1900', 
        verbose_name='year of published'
        )
    short_des = models.CharField(
        max_length=300, 
        blank=True, 
        help_text='description', 
        verbose_name='short description'
        )
    genre = models.ManyToManyField(Genre, help_text = 'genre')
    image = models.ImageField(
        upload_to='media/images/',
        help_text='Cover image', 
        blank=True, 
        verbose_name='cover image',
        )    

    def display_genre(self) -> str:
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'
    
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к подробной записи этой книги."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.title