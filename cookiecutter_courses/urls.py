
from django.urls import path
from django.contrib import admin

from . import views  # Import your views module
from cookiecutter_courses.views import get_courses, CourseListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'list/', get_courses, name='get_courses_list'
    ),
    path('v1/list/', CourseListAPIView.as_view(), name='courselist')
]
