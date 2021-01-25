from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.

class HelloWorld(TemplateView):
    template_name = 'Hello.html'
