from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello_view, name='index'),
]
