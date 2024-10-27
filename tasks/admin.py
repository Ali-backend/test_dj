from django.contrib import admin
from .models import Category, Task

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category']
    list_display_links = ['title']
    search_fields = ['title', 'description']
    list_filter = ['category', 'completed']

admin.site.register(Category)
admin.site.register(Task)
