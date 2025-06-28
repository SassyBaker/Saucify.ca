from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from . import models



# Create your views here.
class ListPage(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = "shop/index.html"
    context_object_name = "categories"
    paginate_by = 100  # if pagination is desired
