from django.db import models

# Create your models here.
class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    description2 = models.TextField(blank=True)

    def __str__(self):
        return self.title