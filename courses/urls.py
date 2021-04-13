from django.urls import path, include
from courses import views
from courses.routers import router

urlpatterns = [
    path('', views.show_courses, name='courses'),
    path('single/<id>', views.show_single_course, name='single_course'),
    path('api/', include(router.urls)),
]