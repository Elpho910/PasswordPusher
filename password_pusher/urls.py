# password_pusher/urls.py

from django.urls import path
from .views import generate_password, generate_link, index, view_password

urlpatterns = [
    path("", index, name="index"),
    path("view/<uuid:link>/", view_password, name="view_password"),
]
