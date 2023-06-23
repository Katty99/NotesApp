from django.urls import path, include

from NotesApp.notes import views

urlpatterns = [
    path('add/', views.add_notes, name='add_notes'),
    path('edit/<int:id>/', views.edit_notes, name='edit_notes'),
    path('delete/<int:id>/', views.delete_notes, name='delete_notes'),
    path('details/<int:id>/', views.details_notes, name='details_notes'),
]