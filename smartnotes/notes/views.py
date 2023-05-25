from django.shortcuts import render
from django.http import Http404
from .models import Note
from django.views.generic import CreateView, DetailView, ListView


# Create your views here.

class NotesCreateView(CreateView):
    model = Note
    fields = ['title', 'text' ]
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


    


