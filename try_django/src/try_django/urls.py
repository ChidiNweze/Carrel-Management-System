"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from pages.views import home_view, register, user_login, edit, select
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('reg_form/', register, name='reg_form'),
    path('login/', user_login, name='login'),
    path('hostels/<slug:hostel_name>/', home_view, name='hostel'), #was  originally views.hostel_detail_view
    path('login/edit/', edit, name='edit'),
    path('login/select/', select, name='select'),
    path('logout/', home_view, name='logout'),
    path('reg_form/login/edit/', edit, name='update'),
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
