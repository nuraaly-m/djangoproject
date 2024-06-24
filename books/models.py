from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):

    GENRE_BOOKS = (
        ("дэтектив", "дэтектив"),
        ("хоррор", "хоррор"),
        ("роман", "роман"),
        ("фантастика", "фантастика"),
    )

    title = models.CharField(max_length=100, verbose_name="введите название книги")
    author = models.CharField(max_length=100, verbose_name="введите имя автора")
    genre = models.CharField(
        max_length=100, choices=GENRE_BOOKS, verbose_name="укажите жанр"
    )
    image = models.ImageField(
        upload_to="images/", verbose_name="загрузите фото", blank=True
    )
    description = models.TextField(verbose_name="добавьте описание книги")
    music = models.FileField(
        upload_to="audios/", verbose_name="загрузите аудио", blank=True
    )
    video = models.URLField(verbose_name="укажите url видео", blank=True)
    price = models.PositiveIntegerField(verbose_name="укажите цену книги")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}--{self.genre}"

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"


class ReviewBooks(models.Model):
    book = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name="review_books"
    )
    text = models.TextField()
    mark = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.book}--{self.mark}"
