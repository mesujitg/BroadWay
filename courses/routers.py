from rest_framework import routers
from courses.viewsets import CourseViewSet

router = routers.DefaultRouter()
router.register('course', CourseViewSet)
