from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from content import models as content_models
from session import mixins as session_mixins


class Skill(session_mixins.StaffRequiredMixin, ListView):
    template_name = 'administration/content/skill.html'
    model = content_models.Skill


class SkillCreate(session_mixins.StaffRequiredMixin, CreateView):
    model = content_models.Skill
    template_name = 'administration/content/skill_form.html'
    fields = ['order', 'title', 'category', 'logo', 'is_active']

    def get_success_url(self):
        return reverse('administration:skill')


class SkillUpdate(session_mixins.StaffRequiredMixin, UpdateView):
    model = content_models.Skill
    pk_url_kwarg = 'skill_pk'
    template_name = 'administration/content/skill_form.html'
    fields = ['order', 'title', 'category', 'logo', 'is_active']

    def get_success_url(self):
        return reverse('administration:skill')


class SkillDelete(session_mixins.StaffRequiredMixin, DeleteView):
    model = content_models.Skill
    pk_url_kwarg = 'skill_pk'
    template_name = 'administration/content/skill_delete.html'

    def get_success_url(self):
        return reverse('administration:skill')
