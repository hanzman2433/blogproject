from django.contrib import admin
from .models import SampleModel, BlogModel


admin.site.register(SampleModel)
admin.site.register(BlogModel)