from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Flight


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "flights/index.html"
    context_object_name = "all_user_flights"

    def get_queryset(self):
        return Flight.objects.filter(owner=self.request.user)


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Flight
    template_name = "flights/detail.html"


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Flight
    fields = ["name", "description"]
    template_name = "flights/create_update.html"


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Flight
    template_name = "flights/detail.html"
    success_url = reverse_lazy("flights:list")


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Flight
    fields = ["name", "description", "data_file"]
    template_name = "flights/create_update.html"

    @transaction.atomic
    def form_valid(self, form):
        # response = super(CreateView, self).form_valid(form)
        # # do something with self.object
        # return response
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj = obj.save(reparse=True)
        return HttpResponseRedirect(obj.get_absolute_url())
