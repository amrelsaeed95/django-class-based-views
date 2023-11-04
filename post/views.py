from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post 


class PostList(ListView):
    model = Post 
    


class PostDetail(DetailView):
    model = Post


class PostCreate(): 
    pass   


class PostDelete():
    pass 


class PostUpdate():
    pass 