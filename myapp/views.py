from django.http import HttpResponse, JsonResponse
from .models import Project

# Create your views here.
def helloWord(request):
    return HttpResponse("""
        <h1>hola mundo!!</h1>
    """)
    
def index(request):
    return HttpResponse("""
        <h1>Home Page</h1>
    """)
    
def about(request, username):
    print(username)
    return HttpResponse("""
        <h1>Acerca de Nosotros %s</h1>
    """ % username)
    
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
    
def tasks(request):
    return HttpResponse("""
        <h1>Tareas</h1>
    """)
    
