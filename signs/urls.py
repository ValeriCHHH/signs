from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('signs/', views.sign),
    path('doc/', views.doc),
]
