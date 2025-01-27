from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('params/<int:param1>', views.handle_params, name='HandleParams')
]
