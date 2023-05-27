from django.shortcuts import render
from django.http import Http404
from .models import Note
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm

# Create your views here.

class NotesDeleteView(DeleteView):
    model = Note
    success_url ='/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model= Note
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'

class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'
    
class NotesListView(ListView):
    model = Note
    context_object_name =  "notes"
    template_name = 'notes/notes_list.html'
    
    
class NotesDetailView(DetailView):
    model = Note
    context_object_name =  "note"
    template_name = 'notes/notes_detail.html'



    


