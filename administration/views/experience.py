from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from content import models as content_models
from session import mixins as session_mixins


class Experience(session_mixins.StaffRequiredMixin, ListView):
    template_name = 'administration/content/experience.html'
    model = content_models.Experience


class ExperienceCreate(session_mixins.StaffRequiredMixin, CreateView):
    model = content_models.Experience
    template_name = 'administration/content/experience_form.html'
    fields = ['order', 'title', 'location', 'content', 'image', 'logo', 'is_active', 'date_started', 'date_ended', 'date_published']

    def get_success_url(self):
        return reverse('administration:experience')


class ExperienceUpdate(session_mixins.StaffRequiredMixin, UpdateView):
    model = content_models.Experience
    pk_url_kwarg = 'experience_pk'
    template_name = 'administration/content/experience_form.html'
    fields = ['order', 'title', 'location', 'content', 'image', 'logo', 'is_active', 'date_started', 'date_ended', 'date_published']

    def get_success_url(self):
        return reverse('administration:experience')


class ExperienceDelete(session_mixins.StaffRequiredMixin, DeleteView):
    model = content_models.Experience
    pk_url_kwarg = 'experience_pk'
    template_name = 'administration/content/experience_delete.html'

    def get_success_url(self):
        return reverse('administration:experience')
