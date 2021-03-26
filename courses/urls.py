from django.urls import path

from courses import views

urlpatterns = [
    path('', views.show_courses, name='courses')
]