from django.http import HttpResponse

# Create your views here.
def helloWord(request):
    return HttpResponse("""
        <h1>hola mundo!!</h1>
    """)
    
def about(request, username):
    print(username)
    return HttpResponse("""
        <h1>Acerca de Nosotros %s</h1>
    """ % username)