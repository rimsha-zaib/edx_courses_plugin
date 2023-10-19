from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Courses
from rest_framework.generics import ListAPIView
from .serializers import CoursesSerializer
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.course_api.serializers import CourseSerializer

@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    serializer = CoursesSerializer(courses, many=True)
    return Response({'courses': serializer.data})
class CourseListAPIView(ListAPIView):

    queryset = CourseOverview.get_all_courses().prefetch_related(
        'modes',
    ).select_related(
        'image_set'
    )
    serializer_class = CourseSerializer
