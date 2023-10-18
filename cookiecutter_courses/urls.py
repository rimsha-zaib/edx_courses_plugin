
from django.urls import path
from django.contrib import admin

from . import views  # Import your views module
from cookiecutter_courses.views import get_courses

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="courses_catalog/base.html")),
    path('admin/', admin.site.urls),
    path(
        'list/', get_courses, name='get_courses_list'
    )
]