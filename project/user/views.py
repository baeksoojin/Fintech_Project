from django.shortcuts import render,redirect
from user.models import User
from .validation import *

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