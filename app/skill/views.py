from rest_framework import generics
from user.api.permissions import IsAdmin

from .models import Skill
from .serializers import SkillSerializer


class SkillCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillReadView(generics.RetrieveAPIView):
    permission_classes = [IsAdmin]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
