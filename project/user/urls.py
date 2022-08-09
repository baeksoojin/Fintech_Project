from django.urls import path,include
import user.views as views

app_name = 'user'

urlpatterns = [
    path('signup/',views.Signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('connect/',views.Connect,name='connect'),
    path('check/',views.Check,name='check'),
]