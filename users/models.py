from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(
        default=18, validators=[MinValueValidator(5), MaxValueValidator(99)]
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    experience = models.PositiveIntegerField(default=0)
    telegram = models.CharField(max_length=100, blank=True)
    favorite_genre = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default="junior")



@receiver(post_save, sender=CustomUser)
def set_level(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан успешно пользователь зарегистрировался')
        experience = instance.experience
        if experience < 1:
            instance.level = 'junior'
        elif experience >= 1 and experience <= 3:
            instance.level = 'junior'
        elif experience >= 4 and experience <= 6:
            instance.level = 'middle'
        elif experience >= 7 and experience <= 15:
            instance.level = 'senior'
        else:
            instance.level = 'Уровень не определен'
        instance.save()