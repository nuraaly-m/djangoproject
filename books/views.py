from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from books.models import Books


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
