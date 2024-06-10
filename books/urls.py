from django.urls import path
from . import views


urlpatterns = [
    path('bio/', views.bio_view),
    path('hobby/', views.hobby_view),
    path('time/', views.time_view),
    path('random/', views.random_view),
]