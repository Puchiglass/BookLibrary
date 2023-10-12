import uuid

import datetime

from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from library.models import Author, Book, Genre

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 13 авторов для тестов пагинации страниц.
        number_of_authors = 13
        for author_id in range(number_of_authors):
            Author.objects.create(
                first_name='Big', 
                last_name='Bob',
                surename='Denisovich',
                birth_day='1900-01-01'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/author_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        # Получить вторую страницу и подтвердить, что на ней осталось (ровно) 3 элемента
        response = self.client.get(reverse('authors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['author_list']), 3)


class CreateBookByUserViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', 
                                              password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', 
                                              password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        test_author = Author.objects.create(
            first_name='Big', 
            last_name='Bob',
            surename='Denisovich',
            birth_day='1900-01-01'
        )
        test_genre = Genre.objects.create(name='Fantasy')
        test_book = Book.objects.create(
            title='Book Title',
            author=test_author,
            pub_year='1900',
            short_des='Test book description',
            genre = test_genre,
        )

        test_book.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('book-create'))
        self.assertRedirects(response, '/accounts/login/?next=/book/create/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('book-create'))

        # Проверка, что наш пользователь вошел в систему
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Проверка, что мы использовали правильный template
        self.assertTemplateUsed(response, 'library/book_form.html')