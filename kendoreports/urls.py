from django.urls import path
from . import views

urlpatterns = [
    path("kendo/", views.viewKendo, name="viewKendo"),
]
