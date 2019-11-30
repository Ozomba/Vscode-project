from django.urls import include, path
from vscode_app import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about, name='about'),
]