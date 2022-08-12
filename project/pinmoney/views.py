from django.dispatch import receiver
from django.shortcuts import redirect, render
from user.models import User
from pinmoney.models import Pinmoney, Regular
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

    if request.method == "POST":

        username = request.POST['username']

        res_data['username'] = username
        
        pinmoney = Pinmoney
        if pinmoney.objects.filter(username = member.id).exists():
            print("member의 transaction이 존재합니다")
            transaction = pinmoney.objects.filter(username = member.id)
            res_data['transaction'] = transaction
        print(member)
        return render(request,'pinmoney/give.html',res_data)

           
    else:
        res_data = get_family(request)
        return render(request,'pinmoney.html',res_data)

def transaction(request):

    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인
    res_data={}
    if request.method=="POST":
        try:
            receiver =request.POST['receiver']
            text =request.POST['text']
            amount =int(request.POST['amount'])
            print(receiver,text,amount)
            now = datetime.now()
            current_time = now.strftime('%Y-%m-%d %H:%M:%S')
            print(current_time)
            date = current_time

            res_data['receiver'] = receiver
            res_data['amount']=amount
            #save
            pinmoney = Pinmoney
            pinmoney(username=member,date = now, amount = amount, text= text, receiver=receiver).save()
            
            return render(request,'pinmoney/certification.html',res_data)
        except:
            opponent=request.POST['opponent']
            res_data['opponent'] = opponent
            return render(request,'pinmoney/transaction.html',res_data)
    else:
        res_data = get_family(request)
        return render(request,'pinmoney.html',res_data)

def certification(request):

    if request.method=="POST":
        res_data={}
        pinmoney = Pinmoney
        last_pinmoney = pinmoney.objects.last()
        print(last_pinmoney)
        print("========>",last_pinmoney.receiver, last_pinmoney.amount, last_pinmoney.text)
        res_data['last_pinmoney'] = last_pinmoney
        res_data['receiver']=last_pinmoney.receiver
        res_data['amount']=last_pinmoney.amount
        res_data['text']=last_pinmoney.text
        print(res_data)
        return render(request,'pinmoney/success.html',res_data)
    else:
        return render(request,'pinmoney/certification.html')

def success(request):

    if request.method=="POST":
        success = request.POST['success']
        print(success)
        res_data = get_family(request)
        return render(request,'pinmoney.html',res_data)
    else:
        print("here")
        return render(request,'pinmoney/success.html')

########### 정기적금관련 ###########

def regular(request):

    res_data = get_family(request)
    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인

    regular = Regular

    try:
        if request.method == "POST":
            print("here")
            try:
                receiver = request.POST['receiver']
                unit = request.POST['unit']
                date = request.POST['date']
                type = request.POST['type']
                amount = request.POST['amount']
                go = request.POST['go']
                print(go)

                regular(username=member, unit=unit, date=date, type=type, amount=amount, receiver= receiver).save()
                if regular.objects.filter(username = member.id).exists():
                    print("member의 정기적금 등록 transaction이 존재합니다")
                    transaction = regular.objects.filter(username = member.id)
                    res_data['transaction'] = transaction
                return render(request,'pinmoney/regular_list.html',res_data)

            except:
                back = request.POST['back']
                print(back)
                
                return render(request,'pinmoney.html',res_data)
        else:
            res_data = get_family(request)
            return render(request,'pinmoney/regular.html',res_data)

    except:
        res_data = get_family(request)
        return render(request,'pinmoney/regular.html',res_data)

def Regular_list(request):
    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))#본인

    if request.method=="POST":
        res_data={}
        regular = Regular
        transaction = regular.objects.filter(username = member.id)
        print(transaction)
        res_data['transaction'] = transaction

        return render(request,'pinmoney/regular_list.html',res_data)
    else:
        res_data = get_family(request)
        return render(request,'pinmoney.html',res_data)

