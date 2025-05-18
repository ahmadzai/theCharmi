from django.contrib import admin
from .models import HomeContent, Slider


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_by', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('title', 'subtitle')

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'small_title', 'button_link', 'updated_by', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('small_title', 'title', 'text')

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
