from django.views.generic import ListView, TemplateView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

class BlogListView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ImputPageView(TemplateView):
    template_name = 'imput.html'