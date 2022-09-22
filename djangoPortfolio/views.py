from django.views.generic import TemplateView
from content import models as content_models
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from sendemail import forms as contact_form
from django.core.mail import send_mail


class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data()
        context['experience'] = content_models.Experience.objects.all()[:6]
        context['skill'] = content_models.Skill.objects.all()
        context['project'] = content_models.Project.objects.all()[:6]
        context['contactform'] = contact_form.ContactForm()
        if 'section' in kwargs:
            context['section'] = kwargs['section']

        return context

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            contactform = contact_form.ContactForm(self.request.POST)
            print(contactform)
            if contactform.is_valid():
                print('the form is valid')
                firstname = contactform.cleaned_data["firstname"]
                from_email = contactform.cleaned_data["from_email"]
                message = contactform.cleaned_data['message']
                html = render_to_string('contactform.html', {
                    'firstname': firstname,
                    'from_email': from_email,
                    'message': message,
                })
                send_mail(firstname, from_email, message, ['a.pillois@gmail.com'], html_message=html)
                return redirect('homepage')
            else:
                print('form not valid')
        else:
            contactform = contact_form.ContactForm()
        return render(self.request, 'homepage.html', {
            'contactform': contactform
        })
