from rest_framework import viewsets
from  rest_framework.permissions import AllowAny
from .models import Task
from .serlializers import TaskSerializer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
