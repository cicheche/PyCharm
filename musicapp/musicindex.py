from django.conf import settings
from django.views.generic import ListView, DetailView
from musicapp.models import Musicdata, Comment


class home(ListView):
    template_name = "index.html"
    queryset = Musicdata.objects.order_by("id")
    context_object_name = "music_list"
    paginate_by = 5

class musicdetail(DetailView):
    template_name = "detail.html"
    model = Comment
    context_object_name = "co"