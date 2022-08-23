from django.urls import path
from . import views

app_name = "forecasts"


urlpatterns = [
    path("net-worth/", views.viewNetWorth, name="viewNetWorth"),
]
