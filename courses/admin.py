from django.contrib import admin
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'details', 'fee']


admin.site.register(Course, CourseAdmin)
