from django.http import HttpResponse
from django.views.generic import TemplateView
from content import models as content_models


class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data()
        context['experience'] = content_models.Experience.objects.all()[:6]
        context['skill'] = content_models.Skill.objects.all()[:6]
        context['project'] = content_models.Project.objects.all()[:6]
        if 'section' in kwargs:
            context['section'] = kwargs['section']
        return context

