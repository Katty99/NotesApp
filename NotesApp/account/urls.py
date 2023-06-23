from django.urls import path, include

from NotesApp.account import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile')
]