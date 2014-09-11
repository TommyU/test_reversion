from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView
from .models import article
from django.shortcuts import render_to_response
# Create your views here.

class articleDV(DeleteView):
    model = article
    success_url = "/admin/test_app/article/"
    template_name = "article_delete.html"

class articleUV(UpdateView):
    model = article
    success_url = "/admin/test_app/article/"
    template_name = "article_update.html"