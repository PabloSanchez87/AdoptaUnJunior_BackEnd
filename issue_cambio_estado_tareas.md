
# Issue: Agregar funcionalidad para cambiar el estado de las tareas

## Descripción

Actualmente, la vista de la aplicación `goals_app` muestra las tareas pero no permite a los usuarios cambiar su estado (Pendiente, En progreso, Completado). Esta issue tiene como objetivo agregar la funcionalidad necesaria para que los usuarios puedan cambiar el estado de una tarea específica directamente desde la interfaz de usuario.

## Funcionalidades a Implementar

- **Objetivo**: Permitir que los usuarios cambien el estado de una tarea a través de la interfaz de usuario.
- **Método**: Añadir un menú desplegable o un conjunto de botones junto a cada tarea que permita seleccionar su nuevo estado.

## Pasos para Resolver la Issue

1. **Modificar la Vista para Cambiar el Estado de las Tareas**:
   - Abre el archivo `goals_list.html` ubicado en `goals_app/templates/`.
   - Añade un menú desplegable o botones junto a cada tarea para permitir que los usuarios cambien su estado.
   - El menú desplegable debe tener las siguientes opciones:
     - Pendiente
     - En progreso
     - Completado

2. **Implementar la Lógica de Cambio de Estado**:
   - Crea una nueva vista en `views.py` dentro de `goals_app` que maneje las solicitudes POST para actualizar el estado de una tarea.
   - Asegúrate de que esta vista actualice correctamente el campo `status` en el modelo `Task`.

3. **Actualizar la URL**:
   - Añade una nueva ruta en `urls.py` para manejar la solicitud de cambio de estado. Esta ruta debe apuntar a la nueva vista creada en el paso anterior.

4. **Probar la Funcionalidad**:
   - Navega a la página donde se listan las tareas y verifica que el menú desplegable o los botones funcionan correctamente.
   - Cambia el estado de una tarea y verifica que la actualización se refleje en la base de datos.

5. **Escribir Tests (Opcional, pero recomendado)**:
   - Si tienes tiempo, escribe un test unitario que verifique que el estado de una tarea se puede cambiar correctamente desde la vista.

## Consideraciones Adicionales

- **Control de Errores**: Asegúrate de manejar posibles errores (por ejemplo, si se intenta cambiar el estado de una tarea que no existe).
- **Interfaz de Usuario**: La interfaz debe ser intuitiva y clara. Considera agregar un pequeño mensaje de confirmación cuando el estado de la tarea cambie.

## Ejemplo de Código

Aquí tienes un ejemplo básico de cómo podría implementarse la lógica de cambio de estado:

```python
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from goals_app.models import Task

def change_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        return redirect('goals_list')  # Redirige a la lista de tareas
    return HttpResponse(status=405)  # Método no permitido
```

```html
<!-- En la plantilla goals_list.html -->
<form method="post" action="{% url 'change_task_status' task.id %}">
    {% csrf_token %}
    <select name="status" onchange="this.form.submit()">
        <option value="Pending" {% if task.status == 'Pending' %}selected{% endif %}>Pendiente</option>
        <option value="In Progress" {% if task.status == 'In Progress' %}selected{% endif %}>En progreso</option>
        <option value="Completed" {% if task.status == 'Completed' %}selected{% endif %}>Completado</option>
    </select>
</form>
```

