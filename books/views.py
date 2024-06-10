from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random


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
