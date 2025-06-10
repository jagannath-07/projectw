from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')

def jobform(request):
    return render(request,'jobform.html')