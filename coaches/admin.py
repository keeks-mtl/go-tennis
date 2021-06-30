from django.contrib import admin
from .models import Coach

# Register your models here.


class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'rating',
        'image',
    )

    ordering = ('first_name',)


admin.site.register(Coach, CoachAdmin)
