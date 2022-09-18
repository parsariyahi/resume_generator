from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.ExperienceCreateView.as_view()),
    path("read/<int:pk>/", views.ExperienceReadView.as_view()),
    path("update/<int:pk>/", views.ExperienceUpdateView.as_view()),
    path("delete/<int:pk>/", views.ExperienceDeleteView.as_view()),
]
