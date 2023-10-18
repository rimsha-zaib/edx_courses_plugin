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


from django.apps import AppConfig
# from edx_django_utils.plugins.constants import (
#      PluginURLs, PluginSettings, PluginContexts
# )

from edx_django_utils.plugins import ( 
    PluginSettings, 
    PluginURLs,  
    PluginSignals,  
    PluginContexts, 
)

from openedx.core.djangoapps.plugins.constants import ProjectType


class CookiecutterCoursesConfig(AppConfig):
    """
    Configuration for the courses_catalog Django application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cookiecutter_courses'
    


    plugin_app = {
    
        PluginURLs.CONFIG: {
                'lms.djangoapp': {
                    PluginURLs.NAMESPACE: 'cookiecutter_courses',
                    PluginURLs.APP_NAME: 'cookiecutter_courses',
                    PluginURLs.REGEX: r'^api/cookiecutter_courses/',
                    PluginURLs.RELATIVE_PATH: 'api.urls',
                }
            },
        PluginSettings.CONFIG: {

            'lms.djangoapp': {
                'production': {
                    PluginSettings.RELATIVE_PATH: 'settings.production',
                },
                'common': {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            }
        },
        PluginContexts.CONFIG: {
            'lms.djangoapp': {
                'course_dashboard': 'my_app.cookiecutter_courses.get_dashboard_context'
            }
        }
    }



    # plugin_app = {
    #     PluginURLs.CONFIG: {
    #         ProjectType.LMS: {
    #             PluginURLs.NAMESPACE: 'cookiecutter_courses',
    #             PluginURLs.REGEX: r'^api/cookiecutter_courses/',
    #             PluginURLs.RELATIVE_PATH: 'urls',
    #         }
    #     }
    # }