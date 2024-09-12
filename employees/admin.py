from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'photo')
    list_filter = ('date_of_birth',)
    search_fields = ('first_name', 'last_name', 'email', 'mobile')
    ordering = ('-date_of_birth',)
    readonly_fields = ('photo',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing employee
            return self.readonly_fields + ('photo',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        # Optionally, you can add custom save logic here
        super().save_model(request, obj, form, change)
