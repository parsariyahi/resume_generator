from rest_framework import generics
from user.api.permissions import IsAdmin

from .models import Project
from .serializers import ProjectSerializer

# Create your views here.


class ProjectCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectReadView(generics.RetrieveAPIView):
    permission_classes = [IsAdmin]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
