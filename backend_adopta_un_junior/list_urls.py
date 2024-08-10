import os
import django
from django.urls import URLPattern, URLResolver
from django.urls import get_resolver

# Establece la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_adopta_un_junior.settings')
django.setup()

def list_urls(lis, acc=None, base=''):
    if acc is None:
        acc = []

    for entry in lis:
        if isinstance(entry, URLPattern):
            # Filtrar las rutas que no son generadas automáticamente
            if not any(char in str(entry.pattern) for char in ['<', '>', '^', '$', '?P']):
                acc.append(base + str(entry.pattern))
        elif isinstance(entry, URLResolver):
            # Concatenar el prefijo de ruta
            list_urls(entry.url_patterns, acc, base + str(entry.pattern))

    return acc

if __name__ == "__main__":
    urlpatterns = get_resolver().url_patterns
    urls = list_urls(urlpatterns)
    for url in urls:
        print(url)
