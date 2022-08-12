from django.urls import path, include
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.home ,name="home"),
    path('enjoy',views.enjoy,name = "enjoy"),
    path('pinmoney',views.pinmoney,name = "pinmoney"),
    path('mylogin',views.mylogin,name = "mylogin"),
    path('mypage',views.mypage,name = "mypage"),
    path('mission',views.mission,name = "mission"),
    path('benefit',views.benefit,name = "benefit"),
]
