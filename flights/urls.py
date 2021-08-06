from django.urls import path

from . import views

app_name = "flights"

urlpatterns = [
    path("", views.IndexView.as_view(), name="list"),
    path("create", views.CreateView.as_view(), name="create"),
    path("<uuid:pk>", views.DetailView.as_view(), name="detail"),
    path("<uuid:pk>/update", views.UpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete", views.DeleteView.as_view(), name="delete"),
    path("<uuid:pk>/preview", views.PreviewView.as_view(), name="preview"),
]
