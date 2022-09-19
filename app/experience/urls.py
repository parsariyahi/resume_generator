from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.ExperienceCreateView.as_view(), name='experience_create'),
    path("read/<int:pk>/", views.ExperienceReadView.as_view(), name='experience_read'),
    path("update/<int:pk>/", views.ExperienceUpdateView.as_view(), name='experience_update'),
    path("delete/<int:pk>/", views.ExperienceDeleteView.as_view(), name='experience_delete'),
]
