from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, \
    UpdateAPIView
from api.models import Task
from api.serializers import TaskSerializer


class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GetTaskView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@extend_schema(methods=['PUT'])
class UpdateTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['put']

class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
