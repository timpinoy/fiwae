from django.urls import path
from rest_framework import routers

from . import views

app_name = "finance"
urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("upload_transactions", views.upload_transactions, name="upload_transactions"),
]