from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from flights.models import Flight
from pictures.models import Picture

from .forms import NewUserForm


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = NewUserForm()
    return render(request, "myuser/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            print("form not valid")
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "myuser/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def mapview(request):
    flights = Flight.objects.filter(owner=request.user)
    pictures = Picture.objects.filter(owner=request.user)
    return render(
        request, "map.html", {"flights": flights, "color_step": max(20, 360 / len(flights)), "pictures": pictures}
    )
