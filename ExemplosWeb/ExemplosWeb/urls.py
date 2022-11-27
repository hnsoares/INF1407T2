"""ExemplosWeb URL Configuration

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
from django.urls.conf import include
from ExemplosWeb.views import homepage, homeSec , registro, secreto
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.ProdutoListView.as_view(),name='sec-home'),
    path('accounts/registro/',registro, name = 'sec-registro'),
    path('accounts/profile/',secreto, name='sec-secreta'),

    path('secreto/',secreto, name='sec-secreta'),
    path('secreto/cria',views.ProdutoCreateView.as_view(), name='sec-secreta-create'),
    path('secreto/visualiza',views.ProdutoListViewSec.as_view(),name='sec-secreta-read'),
    path('secreto/atualiza/<int:pk>/',views.ProdutoUpdateView.as_view(),name='sec-secreta-update'),
    path('secreto/deleta/<int:pk>/',views.ProdutoDeleteView.as_view(),name='sec-secreta-delete'),
    path('accounts/login/',LoginView.as_view(template_name = 'registro/login.html'), name = 'sec-login'),
    path('accounts/logout/', LogoutView.as_view(next_page = reverse_lazy('sec-login')),name='sec-logout'),

]
