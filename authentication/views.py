from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'authentication/logged_out.html'

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')
