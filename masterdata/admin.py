from django.contrib import admin
from django.apps import apps
# Register your models here.

for i in apps.all_models.get('masterdata').values():
    admin.site.register(i)
