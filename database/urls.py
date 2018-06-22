from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('input', views.enter),
    path('edit/<int:id>', views.edit),
    path('view/<int:id>', views.view)
]