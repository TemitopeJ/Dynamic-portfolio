from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Skill, About

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    skills = Skill.objects.all()
    abouts = About.objects.all()
    
    return render(request, 'about.html', {'skills': skills})

def contact(request):
    return render(request, 'contact.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})