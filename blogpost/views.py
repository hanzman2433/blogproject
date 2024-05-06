from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView # ←汎用ビュー https://qiita.com/dai-takahashi/items/7d0187485cad4418c073
from .models import BlogModel
from django.urls import reverse_lazy


class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel #ユーザが入力した情報をどこに保存するかを指定している箇所
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')