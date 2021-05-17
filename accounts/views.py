from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "that username already exists")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "that email already exists")
                return redirect("signup")
            else:
                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                print("You are now registered and can log in")
                messages.success(request, "You are now registered and can log in")
                return redirect("login")
        else:
            messages.error(request, "Passwords don't match")
            return redirect("signup")
    else:
        return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        email = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            print("invalid")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    return redirect("index")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
