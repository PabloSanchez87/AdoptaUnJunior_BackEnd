from django.shortcuts import render
from .models import Goal, Task

def goals_list(request):
    goals = Goal.objects.all()
    return render(request, 'goals_list.html', {'goals': goals})

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})


def change_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        return redirect('tasks_list')  # Redirige a la lista de tareas después de actualizar el estado
    return HttpResponse(status=405)  # Método no permitido