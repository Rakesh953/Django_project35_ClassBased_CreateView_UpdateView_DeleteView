from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.http import HttpResponse


class Home(TemplateView):
    template_name='app/Home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(Scname='Qspiders')
    #ordering=['Scname']

def wish(request,n):
    return HttpResponse(f'Hai {n} How are U')


class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class StudentCreate(CreateView):
    model=Student
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'







