from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Project_file)
admin.site.register(Project_image)
admin.site.register(Project_Video)
admin.site.register(Project_constants)
admin.site.register(Update_project)
admin.site.register(Update_cache_table)
