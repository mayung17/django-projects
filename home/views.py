from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = 'smart/'

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('note.list')
        return super().get(request, *args, **kwargs)

class LoginInterface(LoginView):
    template_name = 'home/login.html'

class LogoutInterface(LogoutView):
    template_name = 'home/logout.html'
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class RestrictView(LoginRequiredMixin, TemplateView):
    template_name ='home/restricted.html'
    login_url = '/admin'

