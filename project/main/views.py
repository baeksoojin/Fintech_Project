from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def enjoy(request):
    return render(request,'enjoy.html')

def pinmoney(request):
    return render(request,'pinmoney.html')

def mylogin(request):
    return render(request,'login_index.html')
