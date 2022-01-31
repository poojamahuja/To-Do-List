from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOfObject


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOfObject]
