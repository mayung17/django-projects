from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name='note.list'),
    path('<int:pk>', views.DetailView.as_view(),name="note.detail"),
    path('<int:pk>/edit', views.NotesUpadteView.as_view(), name="note.update"),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name="note.delete"),
    path('create',views.NotesCreateView.as_view(), name="notes.new")

]