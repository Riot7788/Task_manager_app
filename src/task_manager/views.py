from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        telegram_user_id = self.request.query_params.get('telegram_user_id')
        if telegram_user_id:
            return self.queryset.filter(telegram_user_id=telegram_user_id)
        return self.queryset