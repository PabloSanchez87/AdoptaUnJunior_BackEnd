# Backend Adopta un Junior

Este proyecto es una aplicación backend construida con Django, diseñada para gestionar diferentes aspectos del aprendizaje y las metas de un desarrollador backend. La aplicación permite gestionar motivaciones, pasos de aprendizaje y objetivos, incluyendo tareas específicas.


## Índice
1. [Instalación](#instalación)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Uso](#uso)
4. [Modelos](#modelos)
5. [Administración](#administración) 
6. [Contribución](#contribución)
7. [Razones para ser seleccionado para los grupos de trabajo en Adopta un Junior](#razones-para-ser-seleccionado-para-los-grupos-de-trabajo-en-adopta-un-junior)

## Instalación

### Requisitos previos

- Python 3.12
- Django
- pip

### Instrucciones

1. Clona este repositorio:

    ```sh
    git clone https://github.com/tuusuario/backend_adopta_un_junior.git
    cd backend_adopta_un_junior
    ```

2. Crea y activa un entorno virtual:

    ```sh
    python3.12 -m venv .env
    source .env/bin/activate
    ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py makemigrations  
    python manage.py migrate 
    ```

5. (Opcional) Crea un superusuario para acceder al panel de administración:

    ```sh
    python manage.py createsuperuser
    ```

6. Inicia el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

7. Accede a la aplicación en `http://127.0.0.1:8000/`.
   

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
backend_adopta_un_junior/
├── backend_adopta_un_junior/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── templates/
│   │   └── _footer_principal.html
├── motivation_app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── motivation_list.html
├── learning_path_app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── learning_path.html
├── goals_app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── goals_list.html
├── home_app/
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── home.html
└── manage.py
```

## Uso

### Gestión de Motivaciones

Puedes gestionar las motivaciones desde el panel de administración de Django o directamente desde la shell de Django.
```sh
python manage.py shell
```

```python
from motivation_app.models import Motivation

# Añadir una motivación
Motivation.objects.create(
    reason="Aprender Django",
    description="Me interesa aprender a crear aplicaciones web con Django."
)
```

### Camino de Aprendizaje

La aplicación también te permite registrar pasos en tu camino de aprendizaje.

```python
from learning_path_app.models import LearningStep

LearningStep.objects.create(
    title="Entender las bases de datos",
    description="Aprender cómo funcionan las bases de datos relacionales."
)
```

### Gestión de Objetivos y Tareas

Puedes crear objetivos a largo plazo y asociarles tareas específicas.

```python
from goals_app.models import Goal, Task

goal = Goal.objects.create(
    term="Mediano plazo",
    description="Convertirme en desarrollador backend junior."
)

Task.objects.create(
    goal=goal,
    title="Completar el curso de Django",
    status="Pending"
)
```

## Modelos

### Motivation

- **reason**: CharField - La razón para motivarse.
- **description**: TextField - Descripción detallada de la motivación.

### LearningStep

- **title**: CharField - El título del paso de aprendizaje.
- **description**: TextField - Descripción detallada del paso.
- **completed**: BooleanField - Indica si el paso ha sido completado.

### Goal

- **term**: CharField - El plazo del objetivo (Corto, Mediano, Largo).
- **description**: TextField - Descripción detallada del objetivo.

### Task

- **title**: CharField - El título de la tarea.
- **goal**: ForeignKey a `Goal` - Relación con el objetivo correspondiente.
- **status**: CharField - Estado de la tarea (Pendiente, En progreso, Completado).

## Administración

El proyecto incluye un panel de administración de Django.

- Acceso a la interfaz de Django Admin: `http://127.0.0.1:8000/admin/`


## Contribución

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir al proyecto:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía tus cambios a tu fork (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

### <u>Proceso de Colaboración</u>
En esta sección, se detalla cómo se manejó la colaboración en el proyecto.

**Issue Creada**
- Se identificó la necesidad de permitir que los usuarios cambien el estado de las tareas desde la interfaz. 
- La issue fue documentada con pasos específicos para su resolución.
  
  [Link del Issue](https://github.com/PabloSanchez87/AdoptaUnJunior_BackEnd/issues/1)

  [Documento para resolver el Issue](issue_cambio_estado_tareas.md)

**Colaborador Asignado**
- Un colaborador tomó la tarea y comenzó a trabajar en una nueva rama para implementar esta funcionalidad.

**Pull Request (PR)**
- El colaborador envió una Pull Request con los cambios. El código fue revisado y finalmente se aceptó la PR.


## Pasos a seguir para actualizar nuestra rama local con los nuevos cambios
Una vez aceptado el PR, para actualizar nuestra rama local con los nuevos cambios, podemos usar los siguientes comandos:
```sh
#Esto descargará los cambios del remoto, pero no los aplicará en tu rama local todavía
git fetch origin 
```

- *Hacer un merge de los cambios remotos*
```sh
# Fusionar los cambios de la rama main (o cualquier otra rama) con tu rama actual.
# Esto descargará los cambios del remoto, pero no los aplicará en tu rama local todavía:
git fetch origin

git merge origin/main
# Si hay conflictos, Git te lo notificará y te permitirá resolverlos antes de continuar. 

# Una vez que hayas resuelto los conflictos, puedes confirmar los cambios y enviarlos a tu rama remota:
git add .
git commit -m "Merge de los cambios remotos"
git push origin main
```

## Razones para ser seleccionado para los grupos de trabajo en Adopta un Junior

- **Habilidad para Comunicar Ideas y Soluciones**
  
    Más allá de las habilidades técnicas, considero que mi capacidad para comunicar ideas y soluciones de manera clara y efectiva es uno de mis puntos fuertes. 

- **Capacidad para Trabajar en Equipo**

    Creo firmemente que el éxito de cualquier proyecto depende de la colaboración y la capacidad de trabajar bien con los demás. 

- **Adaptabilidad y Flexibilidad**
 
    En el entorno de desarrollo, las circunstancias pueden cambiar rápidamente. Ya sea que se trate de nuevos requisitos del proyecto, cambios en el alcance o la necesidad de aprender una nueva tecnología sobre la marcha, me considero una persona adaptable. 

- **Enfoque en la Resolución de Problemas**
    
    Más allá de las habilidades técnicas, creo que una de mis fortalezas es mi capacidad para abordar problemas.

- **Compromiso con el Crecimiento Personal y Profesional**
    
    No solo busco mejorar en el aspecto técnico, sino también en mi desarrollo como profesional integral. Estoy comprometido con mi crecimiento tanto en habilidades blandas como en técnicas. Esto incluye mejorar en la gestión del tiempo, la empatía, y la capacidad de recibir y dar feedback de manera constructiva. Creo que este equilibrio me permite contribuir de manera significativa a cualquier equipo en el que forme parte.

- **Proactividad y Toma de Iniciativa**

    Ser proactivo y tomar la iniciativa son características que me ayudan a aportar un valor añadido al equipo, identificando áreas de mejora y proponiendo soluciones antes de que se conviertan en problemas.

Por todas estas razones, considero que soy un candidato ideal para formar parte de los grupos de trabajo de Backend. Mi capacidad para trabajar bien con otros, adaptarme a nuevas situaciones y mantener una comunicación abierta y efectiva complementa mis habilidades técnicas, haciendo de mí un miembro valioso para cualquier equipo.


