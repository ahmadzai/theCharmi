from django.contrib import admin
from .models import ContactInquiry


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_number', 'created_at', 'is_resolved', 'updated_by', 'updated_at')
    list_filter = ('created_at', 'is_resolved')
    search_fields = ('name', 'email', 'mobile_number', 'message')
    actions = ['mark_as_resolved']

    def mark_as_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
    mark_as_resolved.short_description = "Mark selected inquiries as resolved"

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
