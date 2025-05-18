from rest_framework import viewsets, status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        telegram_user_id = self.request.query_params.get('telegram_user_id')
        if telegram_user_id:
            return self.queryset.filter(telegram_user_id=telegram_user_id)
        return self.queryset

    @action(detail=True, methods=['patch'])
    def set_status(self, request, pk=None):
        task = self.get_object()
        status_value = request.data.get('status')
        if status_value not in ['done', 'undone']:
            return Response({'error': 'Недопустимый статус'}, status=status.HTTP_400_BAD_REQUEST)
        task.status = status_value
        task.save()
        return Response(TaskSerializer(task).data)