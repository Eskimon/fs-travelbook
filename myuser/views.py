from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import NewUserForm


def register(request):
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
    return render(request, "signup.html", {"form": form})
