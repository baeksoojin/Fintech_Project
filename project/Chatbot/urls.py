from django.urls import path, include
import Chatbot.views

app_name = 'Chatbot'

urlpatterns = [
    path('',Chatbot.views.chathome, name="chathome"),
    path('chatbot/',Chatbot.views.chatbot,name="chatbot"),
]
