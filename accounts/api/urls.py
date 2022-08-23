from django.urls import path
from . import views

urlpatterns = [
    path("get/", views.getAccounts, name="get"),
    path("get-checkpoints/", views.getCheckpoints, name="getCheckpoints"),
]
