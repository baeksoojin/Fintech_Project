from django.http import JsonResponse
from django.shortcuts import render
from Chatbot.send import ChatbotMessageSender
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def chathome(request):
    context={}
    return render(request, "chatbot/chathome.html",context)

@csrf_exempt
def chatbot(request):
    context= {}
    text = request.GET['text']
    print(text)
    res = ChatbotMessageSender().req_message_send(text)
    print(res.status_code)
    print(json.loads(res.text))
    
    if(res.status_code == 200):
        print(res.text)
        print(type(res.text))
        context['text'] = res.text
        context['flag'] = '0'
        # return render(request, "chatbot/chatbot.html",res_data)
        return JsonResponse(context, content_type='application/json')
   