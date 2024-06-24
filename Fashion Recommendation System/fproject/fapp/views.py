from django.shortcuts import render,redirect

# Create your views here.
def Home(request):
    return render(request,"Home.html")


def index(request):
    return render(request,"index.html")


def About(rqeuest):
    return render(rqeuest,"About.html")


from django.contrib.auth.models import User
from django.contrib import messages
def signup(request):
    if request.method == "POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")

        # user authentication check
        user=User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username is already taken,choose another username.")
            return redirect("/signup")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Successfully")
        return redirect("/login")
    return render(request,"signup.html")

# login page
from django.contrib.auth import authenticate,login
def login_pg(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request,"Invalid Username")
            return redirect('/login')
        p=authenticate(username=username,password=password)

        if p is None:
            messages.error(request,"Invalid Password")
            return redirect("/login")
        else:
            login(request,p)
            return redirect("/index")

    return render(request,"login.html")

# logout
from django.contrib.auth import logout

def logout_pg(request):
    logout(request)
    return redirect('/login')
