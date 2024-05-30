from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


# Модель для ресурса CategoryResource(класс, расширяющий
#  супер-класс ModelResource)
class CategoryResource(ModelResource):
    class Meta:
        # импортируем из shop.models все объекты
        queryset = Category.objects.all()
        resource_name = 'categories'
        # и разрешаем только метод get
        allowed_methods = ['get']


# Модель для ресурса CourseResource(класс, расширяющий
#  супер-класс ModelResource)
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    # метод определяет, как принимаются данные от клиента
    # функция добавляет в принимаемые данные переменную "category_id"   
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    
    # метод определяет, как данные передаются клиенту
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle
