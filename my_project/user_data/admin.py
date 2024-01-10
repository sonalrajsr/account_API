from django.contrib import admin
from .models import student_data
# Register your models here.
class student_data_admin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'current_class', 'roll_number', 'skills')


admin.site.register(student_data, student_data_admin)