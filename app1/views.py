from django.shortcuts import render

# Create your views here.
def registration(request):
    return render(request,'registration.html')

def services(request):
    return render(request,'services.html')