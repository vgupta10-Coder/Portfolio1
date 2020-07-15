from django.contrib import admin
from .models import Semester, Job, Courses, Projects, album, certifications
# Register your models here.
admin.site.register(Semester)
admin.site.register(Courses)
admin.site.register(Job)
admin.site.register(Projects)
admin.site.register(album)
admin.site.register(certifications)