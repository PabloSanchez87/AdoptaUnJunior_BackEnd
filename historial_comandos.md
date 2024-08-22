```sh
python3.12 -m venv .env
source .env/bin/activate
# https://www.toptal.com/developers/gitignore/
touch .gitignore && code .gitignore  

git init

git add .
git commit -m "git init, .gitignore generado con gitignore.io, .env creado"
```

```sh
python3.12 -m pip install --upgrade pip
pip install django
pip freeze > requirements.txt
```

```sh
django-admin startproject backend_adopta_un_junior
cd backend_adopta_un_junior    
python manage.py startapp motivation_app
python manage.py startapp learning_path_app
python manage.py startapp goals_app
```

```sh
python manage.py makemigrations  
python manage.py migrate 
```

```sh 
python manage.py createsuperuser # (opcional)
# user: Admin
# pass: adoptaunjunior
```

```sh
# Creo un script para poder lista fácilmente las urls del proyecto.
python list_urls.py
#Salida
admin/
admin/login/
admin/logout/
admin/password_change/
admin/password_change/done/
admin/autocomplete/
admin/jsi18n/
admin/auth/group/
admin/auth/group/add/
admin/auth/user/
admin/auth/user/add/
motivations/
learning_path/
goals/
tasks/
```

```sh
python manage.py startapp home_app
```

```python
# imports
from motivation_app.models import Motivation
from learning_path_app.models import LearningStep
from goals_app.models import Goal, Task
```

```sh
# Introducimos datos de motivación.
Motivation.objects.create(
    reason="Amor por la Tecnología",
    description="Me apasiona aprender y trabajar con nuevas tecnologías."
)

Motivation.objects.create(
    reason="Resolución de Problemas",
    description="Disfruto encontrando soluciones eficientes a problemas complejos."
)

Motivation.objects.create(
    reason="Trabajo en Equipo",
    description="Creo que el trabajo en equipo es clave para el éxito en cualquier proyecto."
)
```

```python
# Introduccion de datos Learning_path
LearningStep.objects.create(
    title="Fundamentos de Python",
    description="Dominar los conceptos básicos de Python."
)

LearningStep.objects.create(
    title="Bases de Datos",
    description="Aprender a diseñar y gestionar bases de datos relacionales."
)

LearningStep.objects.create(
    title="APIs con Django",
    description="Crear y consumir APIs utilizando Django y Django REST Framework."
)
```

```python
# Introduccion Goal y Task
goal = Goal.objects.create(
    term="Desplegar una Aplicación Django",
    description="Configurar y desplegar una aplicación Django en un servidor."
)

Task.objects.create(
    goal=goal,
    title="Configurar el servidor",
    status="Pending"  # Opcional, ya que "Pending" es el valor predeterminado
)

Task.objects.create(
    goal=goal,
    title="Deploy con Git",
    status="Pending"  # Opcional
)
```

```python
# Verificamos datos
Motivation.objects.all()
LearningStep.objects.all()
Goal.objects.all()
Task.objects.all()
```

# Crear una Issue y resolverla

Después de que el colaborador Felix Serrano haya realizado las tareas de la issue.
Realizado el merge
Realizamos un pull de los cambios a nuestro repositorio local:

```sh
#Esto descargará los cambios del remoto, pero no los aplicará en tu rama local todavía
git fetch origin 

git pull origin main
```
# 
Si el colaborador no hubiera hecho el merge de las ramas, lo pasos a seguir serían los siguientes.
````sh

# Opción 1. Hacer un merge de los cambios remotos:
# Ahora, puedes fusionar los cambios de la rama main (o cualquier otra rama) con tu rama actual.
# Esto descargará los cambios del remoto, pero no los aplicará en tu rama local todavía:
git fetch origin
git merge origin/main
# Si hay conflictos, Git te lo notificará y te permitirá resolverlos antes de continuar. 
# Una vez que hayas resuelto los conflictos, puedes confirmar los cambios y enviarlos a tu rama remota:
git add .
git commit -m "Merge changes from main branch"
git push origin main

# Opción 2. Hacer un rebase de los cambios remotos:
# Esto te permitirá aplicar los cambios de la rama main (o cualquier otra rama) sobre tu rama actual, sin crear un merge commit:
git fetch origin
git rebase origin/main
# Si hay conflictos, Git te lo notificará y te permitirá resolverlos antes de continuar.
# Una vez que hayas resuelto los conflictos, puedes confirmar los cambios y enviarlos a tu rama remota:
git add .
git commit -m "Rebase changes from main branch"
git push origin main

# Opción 3. Hacer un pull request para fusionar los cambios remotos:
# Si no tienes permisos para fusionar directamente en la rama principal, 
# puedes enviar una solicitud de extracción (pull request) al dueño del proyecto. 
# El dueño del proyecto luego puede fusionar los cambios en su rama principal.
# Esto te permitirá mantenerte actualizado con los cambios de la rama principal y colaborar con el equipo.
# Para crear un pull request:
# - Ingresa a GitHub o GitLab en tu navegador.
# - Navega hasta el repositorio donde deseas enviar el pull request.
# - Haz clic en la pestaña "Pull requests".
```

