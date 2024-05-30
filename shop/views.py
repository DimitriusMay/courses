from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


# Определяем функции вида связи модели "Course" 
# с шаблоном "shop/courses.html"
def index(request):
    # получаем из базы данных все курсы
    courses = Course.objects.all()
    # и передаём их в шаблон в виде словаря.
    return render(request, "shop/courses.html", {"courses": courses})


# Функция обработки запроса на получение одного курса.
# В функции есть обработка запроса на несуществующий
# курс - с выдачей ответа 404, плюс обработка запроса
# на существующий курс. 
def single_course(request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    
