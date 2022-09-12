from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.SkillCreateView.as_view()),
    path("read/<int:pk>/", views.SkillReadView.as_view()),
    path("update/<int:pk>/", views.SkillUpdateView.as_view()),
    path("delete/<int:pk>/", views.SkillDeleteView.as_view()),
]
