from django.shortcuts import render
from user.models import User
import json
from mission.models import Mission
from pinmoney.models import Regular, Pinmoney

# Create your views here.

def get_family(request):
    user = User
    print(request.session.get('phoneNumber'))
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
    print(member)
    res_data={}

    jsonDecoder= json.decoder.JSONDecoder()
    family_list = jsonDecoder.decode(member.family)
    print(family_list)

    opponent = user.objects.get(phoneNumber=family_list[0])#상대방
    opponent_name = opponent.username
    print(opponent_name)
    if opponent.kind==False:
        opponent_kind = "손주"
    else:
        opponent_kind = "조부모"

    print(opponent_name)
    res_data['opponent_name'] = opponent_name
    res_data['opponent_kind'] = opponent_kind
    return res_data
    
def home(request):

    try:
        res_data = get_family(request)
        return render(request,'index.html',res_data)
    except:
        return render(request,'index.html')

    

def enjoy(request):
    try:
        res_data = get_family(request)
        return render(request,'enjoy.html',res_data)
    except:
        return render(request,'enjoy.html')

def pinmoney(request):
    user = User
    print(request.session.get('phoneNumber'))
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인

    try:
        res_data = get_family(request)
        regular = Regular
        pinmoney = Pinmoney
        regular_list = regular.objects.filter(username = member.id)
        res_data['regular_list'] = regular_list
        pinmoney_list = pinmoney.objects.filter(username = member.id)
        res_data['pinmoney_list'] = pinmoney_list
        return render(request,'pinmoney.html',res_data)
    except:
        return render(request,'pinmoney.html')

def mylogin(request):

    return render(request,'login_index.html')

def mypage(request):

    try:
        res_data = get_family(request)
        return render(request,'user/mypage.html',res_data)
    except:
        return render(request,'user/mypage.html')

def mission(request):
    try:
        if request.method=="POST":
            success = request.POST['success']
            print("success")
            res_data = get_family(request)
            missions = Mission
            mission_list = missions.objects.all()
            res_data['mission_list'] = mission_list
            return render(request,'mission.html',res_data)
        else:
            res_data = get_family(request)
            missions = Mission
            mission_list = missions.objects.all()
            res_data['mission_list'] = mission_list
            return render(request,'mission.html',res_data)
    except:
        print("mission_main_2")
        return render(request,'mission.html')

def benefit(request):
    return render(request,'benefit.html',)
