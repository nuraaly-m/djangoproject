from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)



class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.IntegerField(required=True)
    telegram = forms.CharField(required=True)
    favorite_genre = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "name",
            "surname",
            "city",
            "gender",
            "phone_number",
            "age",
            "experience",
            "telegram",
            "favorite_genre",
        )


    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
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
            instance.level = 'уровень не определен'
        instance.save()