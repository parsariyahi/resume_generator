from django.urls import path

from . import views

urlpatterns = [
    path("<resume_link>/", views.Test.as_view())
]
