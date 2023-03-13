from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Taak



class CustomAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-content', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget.attrs.update({'class': 'form-content', 'placeholder': 'Password'})
        self.fields['password'].label = False

class TodoLogin(LoginView):
    template_name = 'base/login.html'
    form_class = CustomAuthForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo-list')

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs.update({'class': 'form-content', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password1'].help_text = None
        self.fields['password1'].widget.attrs.update({'class': 'form-content', 'placeholder': 'Password'})
        self.fields['password1'].label = False
        self.fields['password2'].help_text = None
        self.fields['password2'].widget.attrs.update({'class': 'form-content', 'placeholder': 'Password Confirmation'})
        self.fields['password2'].label = False

class TodoRegister(FormView):
    template_name = 'base/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TodoRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('todo-list')
        return super(TodoRegister, self).get(*args, **kwargs)


class TodoList(LoginRequiredMixin, ListView):
    model = Taak
    context_object_name = 'taken'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taken'] = context['taken'].filter(gebruiker=self.request.user)
        context['count'] = context['taken'].filter(compleet=False).count()
        return context


class TodoDetail(LoginRequiredMixin, DetailView):
    model = Taak
    context_object_name = 'taak'


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Taak
    fields = ['titel', 'beschrijving', 'compleet']
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.gebruiker = self.request.user
        return super(TodoCreate, self).form_valid(form)

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Taak
    fields = ['titel', 'beschrijving', 'compleet']
    success_url = reverse_lazy('todo-list')

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Taak
    success_url = reverse_lazy('todo-list')









