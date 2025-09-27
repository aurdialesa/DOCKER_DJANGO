from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bienvenido al Gestor Académico</h1>
        <p>Selecciona una opción:</p>
        <ul>
            <li><a href="/admin/">Panel de Administración</a></li>
            <li><a href="/api/">API</a></li>
        </ul>
    """)
