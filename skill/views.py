from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.api.permissions import IsAdmin, IsOwner
from .models import Skill
from .serializers import SkillSerializer

class SkillCreateView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [IsAuthenticated]


class SkillReadView(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [IsOwner]


class SkillUpdateView(generics.UpdateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDeleteView(generics.DestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
