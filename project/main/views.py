from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def enjoy(request):
    return render(request,'enjoy.html')