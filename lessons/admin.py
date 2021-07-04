from django.contrib import admin
from .models import ClassType, Lesson

# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'price',
        'coach',
        'date',
        'spots',
    )

    ordering = ('date',)


class ClassTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(ClassType, ClassTypeAdmin)
