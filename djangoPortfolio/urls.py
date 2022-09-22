"""djangoPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from djangoPortfolio import views as common_views
from django.conf import settings
from django.conf.urls.static import static
from sendemail.views import index
from django.views.static import serve
import debug_toolbar

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', common_views.Homepage.as_view(), name="homepage"),
                  path('administration/', include('administration.urls', namespace="administration")),
                  path(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  # path(r'^sendemail/',  include('sendemail.urls')),
                  path('index/', index, name='index'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#                   path('__debug__/', include(debug_toolbar.urls)),
# urlpatterns += [
#     re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
# ]
