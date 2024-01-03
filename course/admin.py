from django.contrib import admin

# Register your models here.
from .models import Category,Course,Review


class CategoryAdmin(admin.ModelAdmin):
    list_display=['program','math','scince','health']



admin.site.register(Category,CategoryAdmin)
admin.site.register(Course)
admin.site.register(Review)