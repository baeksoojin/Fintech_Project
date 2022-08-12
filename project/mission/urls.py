from django.urls import path,include
import mission.views as views

app_name = 'mission'

urlpatterns = [
    path('give/',views.give,name='give'),
    path('reward/',views.reward,name='reward'),
    path('success/',views.success,name='success'),
    path('self/',views.self,name='self'),
    path('talk/',views.talk,name='talk'),
    
]