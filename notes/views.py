from django.shortcuts import render
from .models import Notes
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NoteDeleteView(DeleteView):
    model = Notes
    success_url ="/smart"
    template_name = 'notes/notes_delete.html'
class NotesUpadteView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart'

class NotesListView(LoginRequiredMixin,ListView):
    # template_name = 'notes/notes_list.html'
    # extra_context = {'notes':Notes.objects.all()}
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class DetailView(DetailView):
    model=Notes
    context_object_name = "note"

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart'

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

def detail(request,pk) :
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note' : note})

