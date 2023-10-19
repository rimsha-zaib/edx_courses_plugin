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
from django.apps import AppConfig​
class CookiecutterCoursesConfig(AppConfig):
    """
    Configuration for the list_and_filter Django application.
    """
​
    name = 'cookiecutter_courses'
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'cookiecutter_courses',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings'},
            }
        },
    } 

​
    # plugin_app = {
    #     PluginURLs.CONFIG: {
    #         ProjectType.LMS: {
    #             PluginURLs.NAMESPACE: 'cookiecutter_courses',
    #             PluginURLs.REGEX: r'^api/cookiecutter_courses/',
    #             PluginURLs.RELATIVE_PATH: 'urls',
    #         }
    #     }
    # }
