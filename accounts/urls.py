from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("create/", views.createAccount, name="create"),
    path("create/institution/", views.createInstitution, name="create_institution"),
    path("balance/update/<int:account_id>/<str:balance>", views.updateBalance, name="updateBalance"),
    path("history/<int:account_id>", views.showAccountHistory, name="history"),
]
