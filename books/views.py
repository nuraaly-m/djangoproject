from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from books.models import Books
from . import forms


def edit_book_view(request, id):
    book_id = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book successfully updated!</h3>'
                                '<a href="/books/">На список книг</a>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='blog/edit_book.html',
                  context={
                      'form': form,
                      'book_id': book_id
                  })


def drop_book_view(request, id):
    book_id = get_object_or_404(Books, id=id)
    book_id.delete()
    return HttpResponse('Book deleted <a href="/books/">На список книг</a>')


def create_book_view(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book successfully created!</h3>'
                                '<a href="/books/">На список книг</a>')
    else:
        form = forms.BookForm()
    return render(request, template_name='blog/create_book.html',
                  context={'form': form})




def all_books(request):
    if request.method == 'GET':
        books = Books.objects.filter().order_by('-id')
        return render(request, template_name='books/all_books.html',
                      context={
                          'books': books})


def for_adults_view(request):
    if request.method == 'GET':
        adults_book = Books.objects.filter(tags__name='взрослые').order_by('-id')
        return render(request, template_name='books/for_adults_view.html',
                      context={
                          'adults_book': adults_book})


def for_teens_view(request):
    if request.method == 'GET':
        teens_book = Books.objects.filter(tags__name='подростки').order_by('-id')
        return render(request, template_name='books/for_teens_view.html',
                      context={
                          'teens_book': teens_book})


def books_list_view(request):
    if request.method == 'GET':
        query = Books.objects.filter().order_by('-id')
        return render(
            request,
            template_name='blog/books_list.html',
            context={
                'books': query
            }
        )


def books_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Books, id=id)
        return render(
            request,
            template_name='blog/books_detail.html',
            context={
                'book_id': book_id
            }
        )


def bio_view(request):
    if request.method == 'GET':
        return HttpResponse('My name is Nuraaly Melisbekov, i am 18 y.o')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('My hobby is reading')


def time_view(request):
    if request.method == 'GET':
        return HttpResponse(f'My time is: {datetime.now()}')


def random_view(request):
    if request.method == 'GET':
        return HttpResponse(f'My random number is: {random.randint(1, 100)}')
