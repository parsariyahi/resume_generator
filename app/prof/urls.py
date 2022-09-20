from django.urls import path

from . import views

urlpatterns = [
    path("<resume_link>/", views.ProfileInformation.as_view())
]
