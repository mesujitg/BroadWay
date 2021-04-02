from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from FirstProject.settings import MEDIA_URL
from courses.forms import CourseForm
from courses.models import Course


@login_required
def show_courses(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request, 'Login First')
    #     return redirect('login')
    courses = Course.objects.all()
    # courses = Course.objects.filter(fee__lte=13000)
    # courses = Course.objects.get(id=1)

    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        messages.success(request, 'Course added')
        return redirect('courses')

    form = CourseForm()
    return render(request, 'courses.html', {'courses': courses, 'form': form,
                                            'MEDIA_URL': MEDIA_URL})
