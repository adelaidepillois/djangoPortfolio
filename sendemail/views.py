from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from sendemail.forms import ContactForm
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            html = render_to_string('contactform.html', {
                'firstname': firstname,
                'from_email': from_email,
                'message': message,
            })
            send_mail(firstname, from_email, message, ['a.pillois@gmail.com'])

            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'index.html', {
        'form': form
    })
