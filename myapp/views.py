from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewTask, CreateNewProject

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

def create_task(request):
    
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                project_id=request.POST['project']
            )
        return redirect('tasks')
    else:
        projects = list(Project.objects.all())
        return render(request, 'create_task.html', {
            'form': CreateNewTask(),
            'projects': projects
        })

def create_project(request):
    
    if request.method == 'POST':
        form = CreateNewProject(request.POST)
        if form.is_valid():
            Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    else:
        return render(request, 'create_project.html', {
            'form': CreateNewProject(),
        })
