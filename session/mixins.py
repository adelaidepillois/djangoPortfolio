# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2017-03-24 23:17:51
# @Last Modified by:   Baptiste
# @Last Modified time: 2017-09-23 14:57:50

from django.shortcuts import redirect
from django.contrib import messages
from seo.models import Seo


class StaffRequiredMixin(object):
    #
    #  Redirect if user is no member of the staff
    #
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin:
            return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
        messages.warning(request, 'Merci de bien vouloir vous connecter')
        response = redirect('administration:login_user')
        response['Location'] += '?next=' + request.path
        return response


class AddSeo:
    def __init__(self, get_response):
        self.get_response = get_response  # One-time configuration and initialization.

    def __call__(self, request):
        print(request.path)
        if request.path == '/':
            seos = Seo.objects.filter(url=request.path)
        else:
            seos = Seo.objects.filter(url__in=request.path)
        seo = seos.first()
        if seo:
            print(seo)
            request.title = seo.title
            request.description = seo.description
        response = self.get_response(request)
        return response
