from django.test import TestCase
from django.urls import reverse

from library.models import Author, Genre, Book, Comment

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name='Big', 
            last_name='Bob',
            surename='Denisovich',
            birth_day='1900-01-01'
        )

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_surename_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('surename').verbose_name
        self.assertEqual(field_label, 'surename')

    def test_surename_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('surename').max_length
        self.assertEqual(max_length, 100)

    def test_short_bio_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('short_bio').verbose_name
        self.assertEqual(field_label, 'short biography')

    def test_short_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('short_bio').max_length
        self.assertEqual(max_length, 300)

    def test_portrait_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('portrait').verbose_name
        self.assertEqual(field_label, 'portrait')

    def test_get_name_with_surename_author(sefl):
        author = Author.objects.get(id=1)
        expect_name = f'{author.first_name} {author.surename} {author.last_name}'
        sefl.assertEqual(author.get_name(), expect_name)
        
    def test_get_name_without_surename_author(sefl):
        author = Author.objects.create(
            first_name='Big', 
            last_name='Bob',
            birth_day='1900-01-01'
        )
        expect_name = f'{author.first_name} {author.last_name}'
        sefl.assertEqual(author.get_name(), expect_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # Это также не удастся, если urlconf не определен.
        self.assertEqual(author.get_absolute_url(), '/author/1')

    def test_object_name_is_first_name_last_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name} {author.last_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_str_author(self):
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), f'{author.first_name} {author.last_name}')


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name = 'test genre')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_get_str_genre(self):
        genre = Genre.objects.get(id=1)
        self.assertEqual(str(genre), genre.name)


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name='Big', 
            last_name='Bob',
            surename='Denisovich',
            birth_day='1900-01-01'
        )
        Genre.objects.create(name = 'test genre')
        Book.objects.create(
            title = 'Test Book',
            author = Author.objects.get(id=1),
            pub_year = '1900',
            short_des = 'bla-bla-bla',
            genre = Genre.objects.get(id=1),
        )

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_pub_year_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('pub_year').verbose_name
        self.assertEqual(field_label, 'year of published')

    def test_short_des_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('short_des').verbose_name
        self.assertEqual(field_label, 'short description')

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # Это также не удастся, если urlconf не определен.
        self.assertEqual(book.get_absolute_url(), '/book/1')

    def test_get_str_book(self):
        book = Book.objects.get(id=1)
        self.assertEqual(str(book), book.title)


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name='Big', 
            last_name='Bob',
            surename='Denisovich',
            birth_day='1900-01-01'
        )
        Book.objects.create(
            title = 'Test Book',
            author = Author.objects.get(id=1),
            pub_year = '1900',
            short_des = 'bla-bla-bla',
        )
        Comment.objects.create(
            book = Book.objects.get(id=1),
            content = 'bla-bla-bla',
            name = 'Bob',
        )

    def test_get_absolute_url(self):
        comment = Comment.objects.get(id=1)
        # Это также не удастся, если urlconf не определен.
        self.assertEqual(comment.get_absolute_url(), reverse('books'))

    def test_get_str_comment(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(
            str(comment), 
            f'Book: {comment.book.title}, name: {comment.name}'
            )