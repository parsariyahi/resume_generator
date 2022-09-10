from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework import generics
# Create your views here.


class ExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceReadView(generics.RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceUpdateView(generics.UpdateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceDeleteView(generics.DestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
