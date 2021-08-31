from django.contrib import admin
from .models import ExtraInfo

class ExtraInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('labx_rut', 'user')
    search_fields = ['labx_rut', 'user__username']
    ordering = ['-labx_rut']

admin.site.register(ExtraInfo, ExtraInfoAdmin)
