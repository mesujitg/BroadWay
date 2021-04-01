from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from FirstProject.settings import MEDIA_URL
from courses.models import Course


@login_required
def show_courses(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request, 'Login First')
    #     return redirect('login')
    courses = Course.objects.all()
    # courses = Course.objects.filter(fee__lte=13000)
    # courses = Course.objects.get(id=1)
    return render(request, 'courses.html', {'courses': courses, 'MEDIA_URL': MEDIA_URL})
