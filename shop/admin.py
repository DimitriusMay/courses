from django.contrib import admin
from . import models


# смена отображения названий на странице /admin/
admin.site.site_header = "Administration panel"
admin.site.index_title = "Courses administration"

# включение отображения настроек на странице /admin/ для
# курсов и их категорий
admin.site.register(models.Category)
admin.site.register(models.Course)

