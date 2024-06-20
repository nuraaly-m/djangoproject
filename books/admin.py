from django.contrib import admin
from books.models import Books, ReviewBooks, Tag

admin.site.register(Books)
admin.site.register(ReviewBooks)
admin.site.register(Tag)