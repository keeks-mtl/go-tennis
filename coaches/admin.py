from django.contrib import admin
from .models import Coach, Comment

# Register your models here.


class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'image',
    )

    ordering = ('first_name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'coach',
        'stars',
        'comment',
        'author',
    )

    ordering = ('coach',)


admin.site.register(Coach, CoachAdmin)
admin.site.register(Comment, CommentAdmin)