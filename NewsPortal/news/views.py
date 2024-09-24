from django.shortcuts import render
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post, Author


class PostList(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

# class AuthorList(ListView):
#     # Указываем модель, объекты которой мы будем выводить
#     model = Author
#     # Поле, которое будет использоваться для сортировки объектов
#     ordering = 'full_name'
#     # Указываем имя шаблона, в котором будут все инструкции о том,
#     # как именно пользователю должны быть показаны наши объекты
#     template_name = 'authors.html'
#     # Это имя списка, в котором будут лежать все объекты.
#     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'author'
#
# class AuthorDetail(DetailView):
#     # Модель всё та же, но мы хотим получать информацию по отдельному товару
#     model = Author
#     # Используем другой шаблон — author.html
#     template_name = 'author.html'
#     # Название объекта, в котором будет выбранный пользователем продукт
#     context_object_name = 'author'
#     pk_url_kwarg = 'id' #>>> тогда в urls надо указать path('<int:id>' вместо int:pk