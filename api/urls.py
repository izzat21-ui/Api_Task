from django.urls import path
from api.views import CreateTaskView, GetTaskView, TaskDetailView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('create-tasks/', CreateTaskView.as_view(), name='create-tasks'),
    path('get-tasks/', GetTaskView.as_view(), name='get-tasks'),
    path('get-tasks/<int:pk>', TaskDetailView.as_view(), name='get_id-tasks'),
    path('update-tasks/<int:pk>', UpdateTaskView.as_view(), name='update-tasks'),
    path('delete-tasks/<int:pk>', DeleteTaskView.as_view(), name='delete-tasks'),
]