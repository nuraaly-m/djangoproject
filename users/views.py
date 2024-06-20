from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares


# register
class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        experience = form.cleaned_data['experience']
        if experience < 1:
            self.object.level = 'junior'
        elif 1 <= experience <= 3:
            self.object.level = 'junior'
        elif 4 <= experience <= 6:
            self.object.level = 'middle'
        elif 7 <= experience <= 15:
            self.object.level = 'senior'
        else:
            self.object.level = 'Уровень не определен'
        self.object.save()
        return response


# authorization
class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


# Logout
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.filter().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experience'] = getattr(self.request, 'experience', 'Уровень не определен')
        return context
