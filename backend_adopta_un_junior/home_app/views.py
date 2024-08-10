from django.shortcuts import render
import django

def list_urls(lis, acc=None, base=''):
    """
    Función recursiva que recorre y lista todas las URLs configuradas en un proyecto Django.
    """
    if acc is None:
        acc = []

    for entry in lis:
        if isinstance(entry, django.urls.URLPattern):
            if not any(char in str(entry.pattern) for char in ['<', '>', '^', '$', '?P']):
                acc.append(base + str(entry.pattern))
        elif isinstance(entry, django.urls.URLResolver):
            list_urls(entry.url_patterns, acc, base + str(entry.pattern))

    return acc

# def home_view(request):
#     """
#     Vista para la página de inicio que lista todas las URLs y las muestra en una plantilla HTML.
#     """
#     urlpatterns = django.urls.get_resolver().url_patterns
#     urls = list_urls(urlpatterns)
#     return render(request, 'home.html', {'urls': urls})
from django.template import engines

def home_view(request):
    template_engine = engines['django'].engine
    print(template_engine.dirs)  # Imprime las rutas donde Django busca las plantillas
    urlpatterns = django.urls.get_resolver().url_patterns
    urls = list_urls(urlpatterns)
    return render(request, 'home.html', {'urls': urls})

