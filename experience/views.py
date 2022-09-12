from rest_framework import generics
from user.api.permissions import IsAdmin

from .models import Experience
from .serializers import ExperienceSerializer

# Create your views here.


class ExperienceCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceReadView(generics.RetrieveAPIView):
    permission_classes = [IsAdmin]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
