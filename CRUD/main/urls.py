from django.urls import path
from .views import *

urlpatterns = [
    path("<int:id>", ListView, name="index"),
    path("", HomeView, name="home"),
    path("create/", CreateView, name="create"),
    path("view/", View, name="view")
]
