from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from experience.serializers import ExperienceSerializer
from language.serializers import LanguageSerializer
from project.serializers import ProjectSerializer
from skill.serializers import SkillSerializer
from project.models import Project
from .models import Prof
from django.shortcuts import get_object_or_404


class Test(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self, *args, **kwargs):
        resume_link = self.kwargs.get("resume_link")
        user = get_object_or_404(Prof, link=resume_link)
        queryset = Project.objects.filter(user_profile=user)
        return queryset
