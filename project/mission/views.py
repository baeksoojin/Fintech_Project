from django.db import reset_queries
from django.dispatch import receiver
from django.shortcuts import redirect, render
from user.models import User
from mission.models import Mission, MissionList
import json
from datetime import datetime

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

def give(request):

    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
    
    res_data={}
    res_data = get_family(request)

    if request.method == "POST":

        try:
            username = request.POST['username']
            choice = request.POST['choice']
            res_data['username'] = username

            missionlists = MissionList
            print(missionlists.objects.get(id=choice))
            print(missionlists.objects.get(id=choice).text)
            

            now = datetime.now()
            mission = Mission
            mission(username = member, receiver=res_data['opponent_name'], date = now ,text=missionlists.objects.get(id=choice).text).save()
            mission_id = mission.objects.last().id
            if mission.objects.filter(username = member.id).exists():
                    mission_id = mission.objects.last().id
                    print(mission_id)
            print("mission_id",mission_id)
            res_data['mission_id'] = mission_id

            return render(request,'mission/reward.html',res_data)

        except:
            username = request.POST['username']
            res_data['username'] = username
            try:
                try:
                    talk = request.POST['talk']
                    print(talk)
                    print("here")
                    return render(request,'mission/talk.html',res_data)
                except:
                    self = request.POST['self']
                    print(self)
                    return render(request,'mission/self.html',res_data)
            except:
                mission = MissionList
                missions = mission.objects.all()
                res_data['missions'] = missions
                return render(request,'mission/give.html',res_data)
                
    else:
       
        return render(request,'mission.html',res_data)

def reward(request):

    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
    res_data=get_family(request)
    if request.method == "POST":

        reward = request.POST['amount']
        print(reward)
        missions = Mission
        mission = missions.objects.last()
        mission.reward = reward
        mission.save()

        mission = missions.objects.last()
        res_data['receiver'] = mission.receiver
        res_data['reward'] = mission.reward
        res_data['text'] = mission.text

        print(res_data)

        return render(request,'mission/success.html',res_data)
    else:
        return render(request, 'mission.html',res_data)

def success(request):

    # if request.method=="POST":
    #     success = request.POST['success']
    #     print(success)
    #     return render(request,'mission.html')
    # else:
    #     print("here")
    return render(request,'mission.html')
    

def self(request):
    user = User
    print(request.session.get('phoneNumber'))
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
    res_data={}

    if request.method=="POST":
        receiver = request.POST['opponent']
        text = request.POST['text']
        print(text)

        now = datetime.now()
        mission = Mission
        mission(username = member, receiver=receiver, date = now ,text=text).save()
        mission_id = mission.objects.last().id
        if mission.objects.filter(username = member.id).exists():
                mission_id = mission.objects.last().id
                print(mission_id)
        print("mission_id",mission_id)
        res_data['mission_id'] = mission_id
        res_data['username'] =receiver

        return render(request,'mission/reward.html',res_data)
    
    else:
        return render(request,'mission/self.html')


