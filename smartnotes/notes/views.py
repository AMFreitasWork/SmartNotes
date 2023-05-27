from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Note
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
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

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = '/smart/notes' 
    form_class = NotesForm
    login_url= "/admin"   
    template_name = 'notes/notes_form.html'
            
    def form_valid(self, form):
        self.object= form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect (self.get_success_url())
    
    
    
class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name =  "notes"
    template_name = 'notes/notes_list.html'
    login_url="/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
    
class NotesDetailView(DetailView):
    model = Note
    context_object_name =  "note"
    template_name = 'notes/notes_detail.html'



    


