from django.urls import path
from usuarios.views import login, cadastro, logout

urlpatterns = [
    path("teste", login, name="teste"),
    path("cadastro", cadastro, name="cadastro"),
    path("logout", logout, name="logout"),
]
