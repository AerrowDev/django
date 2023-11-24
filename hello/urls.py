from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("<str:name>", views.greet, name="greet"),
  path("aaron", views.aaron, name="aaron"),
  path("John", views.john, name="John"),
 ] 