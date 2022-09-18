from rest_framework import generics
from user.api.permissions import IsAdmin

from .models import Language
from .serializers import LanguageSerializer


class LanguageCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageReadView(generics.RetrieveAPIView):
    permission_classes = [IsAdmin]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
