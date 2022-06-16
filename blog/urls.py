from django.urls import URLPattern, path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),
]