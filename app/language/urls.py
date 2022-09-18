from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.LanguageCreateView.as_view()),
    path("read/<int:pk>/", views.LanguageReadView.as_view()),
    path("update/<int:pk>/", views.LanguageUpdateView.as_view()),
    path("delete/<int:pk>/", views.LanguageDeleteView.as_view()),
]
