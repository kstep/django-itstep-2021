"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

import students.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('todo/', include('todo.urls')),



    path('', RedirectView.as_view(url=reverse_lazy('todo-index'))),

    path('feedback/', include('feedback.urls')),

    path('i18n', include('django.conf.urls.i18n')),  # /i18n/setlang
    path('setlang', set_language),  # /setlang

    path('students/', include('students.urls')),

    ##path('cicd/', include('cicd.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += i18n_patterns(
)


