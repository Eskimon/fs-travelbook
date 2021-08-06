from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Flight


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "flights/index.html"
    context_object_name = "all_user_flights"

    def get_queryset(self):
        return Flight.objects.filter(owner=self.request.user)


class DetailView(generic.DetailView):
    model = Flight
    template_name = "flights/detail.html"

    def get(self, request, *args, **kwargs):
        response = super(DetailView, self).get(request)
        if self.object.is_public or (request.user == self.object.owner):
            return response
        raise Http404()


class PreviewView(generic.DetailView):
    model = Flight
    template_name = "flights/preview.html"

    def get(self, request, *args, **kwargs):
        if request.META["REMOTE_ADDR"] in settings.PREVIEW_ALLOWED_IPS:
            return super(PreviewView, self).get(request)
        return HttpResponseForbidden("<h1>Forbidden</h1>")


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Flight
    fields = ["name", "description", "is_public"]
    template_name = "flights/create_update.html"

    def get_queryset(self):
        queryset = super(UpdateView, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Flight
    template_name = "flights/detail.html"
    success_url = reverse_lazy("flights:list")

    def get_queryset(self):
        queryset = super(DeleteView, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Flight
    fields = ["name", "description", "data_file", "is_public"]
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
