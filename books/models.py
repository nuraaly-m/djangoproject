from django.db import models


class Books(models.Model):

    GENRE_BOOKS = (
        ('дэтектив', 'дэтектив'),
        ('хоррор', 'хоррор'),
        ('роман', 'роман'),
        ('фантастика', 'фантастика')
    )

    title = models.CharField(max_length=100, verbose_name='введите название книги')
    author = models.CharField(max_length=100, verbose_name='введите имя автора')
    genre = models.CharField(max_length=100, choices=GENRE_BOOKS, verbose_name='укажите жанр')
    image = models.ImageField(upload_to='images/', verbose_name='загрузите фото', blank=True)
    description = models.TextField(verbose_name='добавьте описание книги')
    music = models.FileField(upload_to='audios/', verbose_name='загрузите аудио', blank=True)
    video = models.URLField(verbose_name='укажите url видео', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену книги')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}--{self.genre}'


    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'