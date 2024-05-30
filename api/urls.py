from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

# создание экземпляра класса api с номером версии - для класса Api
api = Api(api_name="v1")
# создание экземпляров двух классов и регистрация их в api
category_resource = CategoryResource()
course_resource = CourseResource()
api.register(course_resource)
api.register(category_resource)


# определение маршрутов для доступа пользователей к приложениям:
# /api/v1/courses/       GET, POST для курсов
# /api/v1/courses/1/     GET, DELETE для одного из курсов
# /api/v1/categories/    GET для категорий курсов
# /api/v1/categories/1/  GET для одной категории курсов
urlpatterns = [
    path('', include(api.urls), name='index')
]