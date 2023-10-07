from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetail.as_view(), name='book-detail'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('succes/', views.succes, name='succes'),
    path('register/', views.register_request, name='register'),
    path('search/', views.SearchResultsBook.as_view(), name='search_results'),
    path('comment-create/', views.CommentCreate.as_view(), name='comment-create'),
]