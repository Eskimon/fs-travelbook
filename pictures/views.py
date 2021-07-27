from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from flights.models import Flight

from .models import Picture


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "pictures/index.html"

    def get_queryset(self):
        return Picture.objects.filter(owner=self.request.user)


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Picture
    template_name = "pictures/detail.html"


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Picture
    fields = ["name", "description", "flight", "lat", "lon"]
    template_name = "pictures/create_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flight.objects.filter(owner=self.request.user).all()
        return context


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Picture
    template_name = "pictures/detail.html"
    success_url = reverse_lazy("pictures:list")


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Picture
    fields = ["name", "description", "data_file", "flight", "lat", "lon"]
    template_name = "pictures/create_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flight.objects.filter(owner=self.request.user).all()
        return context

    @transaction.atomic
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())
