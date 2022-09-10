from .models import Language
from .serializers import LanguageSerializer
from rest_framework import generics


class LanguageCreateView(generics.CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageReadView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageUpdateView(generics.UpdateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDeleteView(generics.DestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
