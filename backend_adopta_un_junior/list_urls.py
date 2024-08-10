import os
import django
from django.urls import URLPattern, URLResolver
from django.urls import get_resolver

# Establece la configuración de Django
# Esta línea define la variable de entorno 'DJANGO_SETTINGS_MODULE' para que apunte al archivo settings.py de tu proyecto Django.
# Es esencial para que Django sepa dónde encontrar la configuración del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_adopta_un_junior.settings')

# Configura el entorno de Django
# Llama a django.setup() para configurar Django con la configuración proporcionada, permitiendo el acceso a la funcionalidad completa del framework.
django.setup()

def list_urls(lis, acc=None, base=''):
    """
    Función recursiva que recorre y lista todas las URLs configuradas en un proyecto Django.
    
    Args:
        lis (list): Lista de patrones de URL para procesar.
        acc (list): Acumulador que almacena las rutas URL encontradas.
        base (str): Prefijo base para las URLs (usado en sub-rutas).

    Returns:
        list: Lista de patrones URL filtrados y concatenados.
    """
    
    if acc is None:
        acc = []

    for entry in lis:
        if isinstance(entry, URLPattern):
            # Verifica si la entrada es un URLPattern (una ruta URL)
            # Se filtran las rutas que contienen caracteres especiales como '<', '>', '^', '$', y '?P'
            # Estos caracteres suelen estar presentes en las rutas dinámicas o generadas automáticamente por Django.
            if not any(char in str(entry.pattern) for char in ['<', '>', '^', '$', '?P']):
                # Si la ruta no contiene estos caracteres especiales, se añade al acumulador.
                acc.append(base + str(entry.pattern))
        elif isinstance(entry, URLResolver):
            # Si la entrada es un URLResolver, se trata de un conjunto de subrutas.
            # Se llama recursivamente a list_urls, concatenando el prefijo base con la nueva subruta.
            list_urls(entry.url_patterns, acc, base + str(entry.pattern))

    return acc

if __name__ == "__main__":
    # Obtiene la lista principal de patrones de URL registrados en el proyecto.
    urlpatterns = get_resolver().url_patterns
    
    # Llama a la función list_urls para recorrer las URLs y obtener una lista de URLs filtradas.
    urls = list_urls(urlpatterns)
    
    # Imprime cada URL encontrada.
    for url in urls:
        print(url)
