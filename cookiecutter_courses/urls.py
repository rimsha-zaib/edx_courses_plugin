
from django.urls import path
from django.contrib import admin

from . import views  # Import your views module
from cookiecutter_courses.views import get_courses

urlpatterns = [
    path(
        'list/', get_courses, name='get_courses_list'
    )
]
#helllo
