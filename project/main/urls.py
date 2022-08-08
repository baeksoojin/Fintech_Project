from django.urls import path, include
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.home ,name="home"),
]
