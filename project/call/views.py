from django.shortcuts import render

def index(request):

    return render(request, '../../../Desktop/finproject/Fintech_Project/project/templates/index.html')

def simplecall(request):

    return render(request, 'simpleCall.html')

# Create your views here.
