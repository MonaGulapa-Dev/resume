from django.urls import path
from . import views  # from this current folder, that's the dot means

urlpatterns = [path("", views.home)]

