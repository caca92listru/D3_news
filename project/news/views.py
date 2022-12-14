from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import Post, PostCategory,  Comment
from datetime import datetime

from .filters import PostFilter  # импортируем недавно написанный фильтр
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'News_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

class PostSearch(ListView):
    model = Post
    template_name = 'News_search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 3  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'details/post_detail.html'
    context_object_name = 'news'