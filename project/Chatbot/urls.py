from django.urls import path, include
import Chatbot.views

app_name = 'Chatbot'

urlpatterns = [
    path('chatbot/',Chatbot.views.chatbot,name="chatbot"),
]
