from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Courses
from rest_framework.generics import ListAPIView
from .serializers import CoursesSerializer

@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    serializer = CoursesSerializer(courses, many=True)
    return Response({'courses': serializer.data})

