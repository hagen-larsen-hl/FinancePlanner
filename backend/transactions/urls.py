from django.urls import path
from . import views

app_name = "transactions"


urlpatterns = [
    path("create/", views.createTransaction, name="create"),
    path("view/<int:pk>/", views.viewTransaction, name="view"),
]
