"""
URL configuration for python27 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from python27 import settings
from movies.views import hello_api_view, movie_list_api_view, movie_retrieve_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_api_view),
    path('movies/', movie_list_api_view),
    path('movies/<int:id>/', movie_retrieve_api_view)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)