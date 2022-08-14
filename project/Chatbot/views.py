from django.http import JsonResponse
from django.shortcuts import render
from Chatbot.send import ChatbotMessageSender
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from user.models import User


def chathome(request):
    print("here!!!")
    context={}
    return render(request, "chatbot/chathome.html",context)

@csrf_exempt
def chatbot(request):
    try:
        context= {}
        text = request.GET['text']

        user = User
        print(request.session.get('phoneNumber'))
        member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
        print(member)
        jsonDecoder= json.decoder.JSONDecoder()
        family_list = jsonDecoder.decode(member.family)
        print(">>>>>>>>>>>>>>>>>>>>",family_list)
        print(family_list[0])
        opponent = user.objects.get(phoneNumber=family_list[0])#손주
        print(opponent)

        if text == opponent.username:

            print(text,"에게 얼마를 줄까요?")
            text = text+"에게 얼마를 줄까요?"
            context['mytext'] = text
            context['flag'] = '0'
            return JsonResponse(context, content_type='application/json')
        else:
            print(text)
            res_data={}
            res = ChatbotMessageSender().req_message_send(text)
            print(res.status_code)
            print(json.loads(res.text))
            
            if(res.status_code == 200):
                print(res.text)
                print(type(res.text))
                context['text'] = res.text
                context['flag'] = '0'
                return JsonResponse(context, content_type='application/json')
            # return render(request, "chatbot/chatbot.html",res_data)
            
    except:
        return render(request, "chatbot/chathome.html",context)

   
def voice(request):

    print("here")

    try:

        context= {}
        text = request.GET['text']

        user = User
        print(request.session.get('phoneNumber'))
        member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
        print(member)
        jsonDecoder= json.decoder.JSONDecoder()
        member_list = jsonDecoder.decode(member.family)
        print(">>>>>>>>>>>>>>>>>>>>",member_list)

        if text in member_list:
            print(text,"에게 얼마를 줄까요?")
            text = text+"에게 얼마를 줄까요?"
            context['text'] = text
            context['flag'] = '0'
            return JsonResponse(context, content_type='application/json')
        else:
            print(text)
            res_data={}
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
      
    except:
        return render(request, "chatbot/chathome.html",context)
