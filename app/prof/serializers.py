from experience.serializers import ExperienceSerializer
from language.serializers import LanguageSerializer
from project.serializers import ProjectSerializer
from rest_framework import serializers
from skill.serializers import SkillSerializer

from .models import Prof


class ProfileInformationSerializer(serializers.Serializer):
    experiences = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Prof
        fields = "__all__"

    def get_experiences(self, obj):
        serializer = ExperienceSerializer(instance=obj.experiences.all(), many=True)
        return serializer.data

    def get_languages(self, obj):
        serializer = LanguageSerializer(instance=obj.languages.all(), many=True)
        return serializer.data

    def get_projects(self, obj):
        serializer = ProjectSerializer(instance=obj.projects.all(), many=True)
        return serializer.data

    def get_skills(self, obj):
        serializer = SkillSerializer(instance=obj.skills.all(), many=True)
        return serializer.data
