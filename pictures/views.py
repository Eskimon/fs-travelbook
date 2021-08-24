from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from flights.models import Flight

from .models import Picture


class IndexView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10
    template_name = "pictures/index.html"

    def get_queryset(self):
        return Picture.objects.filter(owner=self.request.user)


class DetailView(generic.DetailView):
    model = Picture
    template_name = "pictures/detail.html"

    def get(self, request, *args, **kwargs):
        response = super(DetailView, self).get(request)
        if self.object.is_public or (request.user == self.object.owner):
            return response
        raise Http404()


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Picture
    fields = ["name", "description", "flight", "lat", "lon", "is_public"]
    template_name = "pictures/create_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flight.objects.filter(owner=self.request.user).all()
        return context

    def get_queryset(self):
        queryset = super(UpdateView, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Picture
    template_name = "pictures/detail.html"
    success_url = reverse_lazy("pictures:list")

    def get_queryset(self):
        queryset = super(DeleteView, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Picture
    fields = ["name", "description", "data_file", "flight", "lat", "lon", "is_public"]
    template_name = "pictures/create_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flight.objects.filter(owner=self.request.user).all()
        return context

    def get_initial(self):
        initial = super(CreateView, self).get_initial()
        initial = initial.copy()
        flight_id = self.request.GET.get("flight", None)
        if flight_id:
            flight = Flight.objects.get(id=flight_id)
            if flight:
                initial["flight"] = flight.id
        return initial

    @transaction.atomic
    def form_valid(self, form):
        # TODO check that flight belong to user
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())
