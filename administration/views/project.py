from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from content import models as content_models
from session import mixins as session_mixins


class Project(session_mixins.StaffRequiredMixin, ListView):
    template_name = 'administration/content/project.html'
    model = content_models.Project


class ProjectCreate(session_mixins.StaffRequiredMixin, CreateView):
    model = content_models.Project
    template_name = 'administration/content/project_form.html'
    fields = ['category', 'date', 'field', 'location', 'picture', 'is_active', 'content']

    def get_success_url(self):
        return reverse('administration:project')


class ProjectUpdate(session_mixins.StaffRequiredMixin, UpdateView):
    model = content_models.Project
    pk_url_kwarg = 'project_pk'
    template_name = 'administration/content/project_form.html'
    fields = ['category', 'date', 'field', 'location', 'picture', 'is_active', 'content']

    def get_success_url(self):
        return reverse('administration:project')


class ProjectDelete(session_mixins.StaffRequiredMixin, DeleteView):
    model = content_models.Project
    pk_url_kwarg = 'project_pk'
    template_name = 'administration/content/project_delete.html'

    def get_success_url(self):
        return reverse('administration:project')
