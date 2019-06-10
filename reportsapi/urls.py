from django.urls import path, include

urlpatterns = [
    path("api/", include("csvreports.urls")),
    path("api/", include("chartreports.urls")),
    path("api/", include("kendoreports.urls")),
]
