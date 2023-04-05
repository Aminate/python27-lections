from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'post_list.html', {})


# мы создали функцию (def) с именем post_list, 
# которая принимает request в качестве аргумента и возвращает (return) 
# результат работы функции render, которая уже соберёт наш шаблон страницы blog/post_list.html

