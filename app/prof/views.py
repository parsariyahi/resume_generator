from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Prof
from .serializers import ProfileInformationSerializer


class ProfileInformation(APIView):
    def get(self, *args, **kwargs):
        resume_link = self.kwargs.get("resume_link")
        queryset = get_object_or_404(Prof, link=resume_link)
        serializer = ProfileInformationSerializer(queryset)
        return Response(serializer.data)
