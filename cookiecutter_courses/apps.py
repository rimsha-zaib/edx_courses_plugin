from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)
from openedx.core.djangoapps.plugins.constants import ProjectType
class CookiecutterCoursesConfig(AppConfig):
    """
    Configuration for the list_and_filter Django application.
    """
    name = 'cookiecutter_courses'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'cookiecutter_courses',
                PluginURLs.REGEX: r'^api/cookiecutter_courses/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }