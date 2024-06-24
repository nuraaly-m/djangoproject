from django.urls import path
from . import views


urlpatterns = [
    path("all_books/", views.all_books, name="all_books"),
    path("teens_books/", views.for_teens_view),
    path("adults_books/", views.for_adults_view),
    path("", views.BooksListView.as_view(), name="books_list"),
    path("books/<int:id>/", views.BooksDetailView.as_view()),
    path("books/<int:id>/delete/", views.BookDeleteView.as_view()),
    path("books/<int:id>/update/", views.EditBookView.as_view()),
    path("create_book/", views.CreateBookView.as_view()),
    path("search/", views.SearchListView.as_view(), name="search"),
    path("bio/", views.bio_view),
    path("hobby/", views.hobby_view),
    path("time/", views.time_view),
    path("random/", views.random_view),
]
