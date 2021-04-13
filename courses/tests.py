# from django.test import TestCase
import unittest
from courses.models import Course


class TestCourse(unittest.TestCase):
    course = Course()

    def test_add(self):
        course = Course()
        actual_result = course.add(5, 7)
        expected_result = 12
        self.assertEqual(actual_result, expected_result)

    # def test_get(self):
    #     courses = Course.objects.all()
    #     actual_result = len(courses)
    #     expected_result = 6
    #     self.assertEqual(actual_result, expected_result)
