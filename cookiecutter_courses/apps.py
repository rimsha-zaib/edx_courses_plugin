# """
# cookiecutter_courses Django application initialization.
# """

# from django.apps import AppConfig


# class CookiecutterCoursesConfig(AppConfig):
#     """
#     Configuration for the cookiecutter_courses Django application.
#     """
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'cookiecutter_courses'


​
from django.apps import AppConfig
​
from edx_django_utils.plugins.constants import (
    PluginURLs
)
​
from openedx.core.djangoapps.plugins.constants import ProjectType
​
class CookiecutterCoursesConfig(AppConfig):
    """
    Configuration for the list_and_filter Django application.
    """
​
    name = 'cookiecutter_courses'
​
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'cookiecutter_courses',
                PluginURLs.REGEX: r'^api/cookiecutter_courses/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }
