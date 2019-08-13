from django.urls import path

from . import views

urlpatterns = [
    path('echo-username/', views.echo_username),
]
