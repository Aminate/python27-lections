from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):
    return render(request, 'post_list.html', {})


# мы создали функцию (def) с именем post_list, 
# которая принимает request в качестве аргумента и возвращает (return) 
# результат работы функции render, которая уже соберёт наш шаблон страницы blog/post_list.html


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})