from django.urls import path
from . import views

app_name = "budgets"


urlpatterns = [
    path("create/", views.createBudget, name="create"),
    path("<int:pk>/", views.viewBudget, name="view"),
    path("archive/<int:pk>/", views.archiveBudget, name="archive"),
    path("item/delete/<int:pk>/", views.deleteBudgetItem, name="delete"),
]
