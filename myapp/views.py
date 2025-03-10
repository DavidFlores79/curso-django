from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404

# Create your views here.
def helloWord(request):
    return HttpResponse("""
        <h1>hola mundo!!</h1>
    """)
    
def index(request):
    title = 'Django App'
    return render(request, 'index.html', {
        'title': title
    })
    
def about(request):
    return render(request, 'about.html')
    
def projects(request):
    projects = list(Project.objects.all())
    return render(request, 'projects.html', {
        'projects': projects
    })
    
def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = list(Task.objects.all())
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    
