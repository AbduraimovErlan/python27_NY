from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.authorization_view),
    path('registration/', views.registration_view),
]