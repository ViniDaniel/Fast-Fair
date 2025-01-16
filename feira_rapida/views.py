from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from .models import User
# Create your views here.

def home(request):
    return render(request, 'feira_rapida/home.html')
