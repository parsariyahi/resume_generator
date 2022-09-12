from django.urls import path
from . import views
urlpatterns = [
    path("create/", views.ProjectCreateView.as_view()),
    path("read/<int:pk>/", views.ProjectReadView.as_view()),
    path("update/<int:pk>/", views.ProjectUpdateView.as_view()),
    path("delete/<int:pk>/", views.ProjectDeleteView.as_view()),
]
