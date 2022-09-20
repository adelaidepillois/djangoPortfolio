

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from session import mixins as session_mixins
from django.views.generic import ListView


class Dashboard(session_mixins.StaffRequiredMixin, TemplateView):
    """
    Dashboard View
    """
    template_name = 'administration/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        return context
