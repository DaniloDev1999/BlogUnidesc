from pdb import post_mortem
from django.views.generic import DetailView,ListView
# Create your views here
from .models import post

class PostListView(ListView):
    model = post

class DetailView(DetailView):
    model = post