from django.shortcuts import render
from user.models import User
import json

# Create your views here.

def get_family(request):
    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
    res_data={}

    jsonDecoder= json.decoder.JSONDecoder()
    family_list = jsonDecoder.decode(member.family)
    print(family_list)

    opponent = user.objects.get(phoneNumber=family_list[0])#상대방
    opponent_name = opponent.username
    if opponent.kind==False:
        opponent_kind = "손주"
    else:
        opponent_kind = "조부모"

    print(opponent_name)
    res_data['opponent_name'] = opponent_name
    res_data['opponent_kind'] = opponent_kind
    return res_data
    
def home(request):

    res_data = get_family(request)

    return render(request,'index.html',res_data)

def enjoy(request):

    res_data = get_family(request)

    return render(request,'enjoy.html')

def pinmoney(request):

    res_data = get_family(request)

    return render(request,'pinmoney.html', res_data)

def mylogin(request):

    return render(request,'login_index.html')

def mypage(request):

    res_data = get_family(request)

    return render(request,'user/mypage.html',res_data)
