from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class LoginUser(TemplateView):
    template_name = 'administration/login.html'

    def post(self, request, *args, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        nextpage = request.GET.get('next', False)
        user = authenticate(email=username, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            if nextpage:
                return redirect(nextpage)
            return redirect('administration:dashboard')
        else:
            context['errors'] = "Identifiants incorrects"
        return render(request, 'administration/login.html', context)


class LogoutUser(RedirectView):
    permanent = False
    pattern_name = 'administration:login_user'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
