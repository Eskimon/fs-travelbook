from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic

from flights.models import Flight
from pictures.models import Picture

from .forms import NewUserForm
from .models import MyUser


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
                return redirect("map")
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
    flights = Flight.objects.filter(owner=request.user)  # .prefetch_related("waypoints")
    # pictures = Picture.objects.filter(owner=request.user)
    pictures = Picture.objects.filter(owner=request.user).order_by("-created")[:100]
    # pictures = []
    return render(
        request,
        "map.html",
        {"flights": flights, "color_step": max(20, 360 / max(1, len(flights))), "pictures": pictures},
    )


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MyUser
    fields = ["icons", "maps"]
    template_name = "myuser/profile.html"

    def get_queryset(self):
        queryset = super(UpdateView, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def form_valid(self, form):
        response = super(UpdateView, self).form_valid(form)
        messages.success(self.request, "Settings updated!")
        return response
