from django.urls import path
from .views import Create, TaskList, deleteTask,updateTask

urlpatterns = [
    path('tasks/create', Create.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', TaskList.as_view(), name='task-detail-delete'),
    path('tasks/', TaskList.as_view(), name='get-all task'),
    path('tasks/delete/<int:id>', deleteTask.as_view(), name='delete task'),
    path('tasks/delete/', deleteTask.as_view(), name='delete task'),
    path('tasks/update/<int:id>', updateTask.as_view(), name='update task'),
    path('tasks/update/', updateTask.as_view(), name='update task'),
    
]
