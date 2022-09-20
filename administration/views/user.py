from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from user.models import AAUser
from session import mixins as session_mixins
from django.http import HttpResponseRedirect


class Users(session_mixins.StaffRequiredMixin, ListView):
    template_name = 'administration/user/users.html'
    model = AAUser


class UserCreate(session_mixins.StaffRequiredMixin, CreateView):
    model =AAUser
    template_name = 'administration/user/user_form.html'
    fields = ['email', 'password']

    def get_success_url(self):
        return reverse('administration:users')

    def form_valid(self, form):
        self.object = form.save()
        print(self.object.password)
        self.object.set_password(self.object.password)
        print(self.object.password)
        self.object.is_admin = True
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserUpdate(session_mixins.StaffRequiredMixin, UpdateView):
    model = AAUser
    pk_url_kwarg = 'user_pk'
    template_name = 'administration/user/user_form.html'
    fields = ['email', 'password']

    def get_success_url(self):
        return reverse('administration:users')


class UserDelete(session_mixins.StaffRequiredMixin, DeleteView):
    model = AAUser
    pk_url_kwarg = 'user_pk'
    template_name = 'administration/user/user_delete.html'

    def get_success_url(self):
        return reverse('administration:users')
