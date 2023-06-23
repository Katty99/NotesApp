from django.urls import path, include

from NotesApp.common import views

urlpatterns = [
    path('', views.home, name='home')
]