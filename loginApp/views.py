from django.shortcuts import render
from .models import User
from django.contrib import messages



# Create your views here.

def login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username,password=password).exists():
            return render(request,"next_page.html")
        else:
            messages.add_message(request, messages.ERROR, "Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")