from django.urls import path
from . import views

urlpatterns = [
    path("csv/", views.downloadCsv, name="downloadCsv"),
]
