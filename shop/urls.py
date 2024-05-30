from django.urls import path
from . import views

# Определение маршрутов.
app_name = 'shop'
urlpatterns = [
    # корневой маршрут, определено имя для возможности
    # перехода между разными страницами.
    path('', views.index, name='index'),
    # определение маршрута страницы по её идентификатору.
    path('<int:course_id>', views.single_course, name='single_course'),
]