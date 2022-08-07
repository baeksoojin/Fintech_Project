from django.shortcuts import render,redirect
from user.models import User
from .validation import *
import json

# Create your views here.
def Signup(request):

    if request.method == "POST":
        
        username = request.POST['username']
        pw = request.POST['pw']
        pw2 = request.POST['pw2']
        phoneNumber = request.POST['phoneNumber']
        print(username,phoneNumber)

        res_data={}

        if pw!=pw2:
            res_data['error'] = "비밀번호가 일치하지 않습니다."
            return render(request,"user/signup.html",res_data)
        if username == "" or phoneNumber == "" or pw == "" or pw2 == "":
            res_data['error'] = "입력되지 않은 값이 있습니다."
            return render(request,"user/signup.html",res_data)
        if "true_pw" != validate_password(pw):
            res_data['error'] = "비밀번호는 6자리이상10자리이하."
            return render(request,"user/signup.html",res_data)
        if "false_email" == validate_phone(phoneNumber):
            res_data['error'] = "핸드폰번호가 올바르지 않습니다"
            return render(request,"user/signup.html",res_data)

        member = User

        if member.objects.filter(phoneNumber=phoneNumber).exists():
            res_data['phoneNumber'] = "이미 가입된 핸드폰입니다"
            return render(request,"user/signup.html",res_data)
        if member.objects.filter(username=username).exists():
            res_data['error'] = "이미 있는 닉네임입니다"
            return render(request,"user/signup.html",res_data)
        else:
            member(username = username, phoneNumber = phoneNumber, password = pw).save()
            return redirect('/')

    else: 
        return render(request,'user/signup.html')

def Login(request):
    if request.method == "POST":
        # email = request.POST["email"]
        phoneNumber = request.POST["phoneNumber"]
        pw = request.POST["pw"]

        members= User
        res_data ={}

        if not members.objects.filter(phoneNumber=phoneNumber).exists():
            res_data['error']="회원정보를 찾을 수 없습니다"
            return render(request,'user/login.html',res_data)
        else:
            data = members.objects.get(phoneNumber = phoneNumber)
            if data.password == pw:
                request.session['phoneNumber'] = phoneNumber
                request.session['username'] = data.username
                request.session.permanent = True #자원의 효율적 운영을 위해 true로 놓음
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 일치하지 않습니다"
                return render(request,"user/login.html",res_data)
    else:
        return render(request,"user/login.html")

def Logout(request):
    #session을 지워주면 됨
    try:#로그아웃했을때 로그인 안 되도록
        if request.session.get('phoneNumber'):
            del request.session['phoneNumber']
    except:
        pass
    return redirect('/')


def Connect(request):
    if request.method == "POST":
        opponent  = request.POST["opponent"]
        phoneNumber = request.POST["phoneNumber"]

        res_data ={}

        #error처리
        member = User
        if not member.objects.filter(phoneNumber=phoneNumber).exists:
            res_data['error'] = "없는 계정입니다"
            return render(request,"user/commect.html",res_data)
            

        if opponent == "grandchild":
            print("손주에게 연결을 요청합니다.")
            #+8201011111111 tester1
            grandch = member.objects.get(phoneNumber=phoneNumber)
            print(grandch.phoneNumber)
            print(request.session.get('phoneNumber'))

            if grandch.connect=='null':
                grandch.connect = json.dumps([request.session.get('phoneNumber')])
                grandch.save()
            else:
                jsonDecoder= json.decoder.JSONDecoder()
                connection_list = jsonDecoder.decode(grandch.connect)
                connection_lists =  connection_list.append(request.session.get('phoneNumber'))
                grandch.connect =  json.dumps(connection_lists)
                grandch.save()

            
        if opponent == "grandparent":
            print("조부모에게 연결을 요청합니다.")
            #+8201098765432 tester2
            grandpa = member.objects.get(phoneNumber=phoneNumber)
            print(grandpa.phoneNumber)

            if not grandpa.connect:
                print("here")
                print([request.session.get('phoneNumber')])
                print(type(json.dumps([request.session.get('phoneNumber')])))
                grandpa.connect = json.dumps([request.session.get('phoneNumber')])
                grandpa.save()
            else:
                jsonDecoder= json.decoder.JSONDecoder()
                connection_list = jsonDecoder.decode(grandpa.connect)
                connection_lists =  connection_list.append(request.session.get('phoneNumber'))
                grandpa.connect =  json.dumps(connection_lists)
                # grandpa.save()


        
        return redirect('/')
    else:
        return render(request,"user/connect.html")
        

def Check(request):
    user = User
    member = user.objects.get(phoneNumber=request.session.get('phoneNumber'))
    if member.connect:
        jsonDecoder= json.decoder.JSONDecoder()
        connection_list = jsonDecoder.decode(member.connect)
        print("현재 connection 요쳥 : ",connection_list[0])
        member2 = user.objects.get(phoneNumber=connection_list[0])
        res_data={}
        res_data['name'] = member2.username
        return render(request,"user/check.html",res_data)
    else:
        res_data['nan'] ="연겨요청이 없습니다"
        return render(request,"user/check.html",res_data)

