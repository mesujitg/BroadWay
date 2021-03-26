from django.shortcuts import render

from FirstProject.settings import MEDIA_URL
from courses.models import Course


def show_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses, 'MEDIA_URL': MEDIA_URL})
