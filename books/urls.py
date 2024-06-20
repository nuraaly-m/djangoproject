from django.urls import path
from . import views


urlpatterns = [
    path('all_books/', views.all_books),
    path('teens_books/', views.for_teens_view),
    path('adults_books/', views.for_adults_view),

    path('books/', views.books_list_view),
    path('books/<int:id>/', views.books_detail_view),
    path('books/<int:id>/delete/', views.drop_book_view),
    path('books/<int:id>/update/', views.edit_book_view),
    path('create_book/', views.create_book_view),

    path('bio/', views.bio_view),
    path('hobby/', views.hobby_view),
    path('time/', views.time_view),
    path('random/', views.random_view),
]
