from django.shortcuts import render, get_object_or_404
from .models import Job, Semester, Courses, Projects, album, certifications


# Create your views here.


def homepage(request):
    jobs = Job.objects.all()
    projects = Projects.objects.all()
    # semester = Semester.objects.all()
    # courses = Courses.objects.all()
    return render(request, 'home.html', {'jobs': jobs, 'projects': projects})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'detail.html', {'jobs': job_detail})


def projectsview(request, proj_id):
    proj_detail = get_object_or_404(Projects, pk=proj_id)
    return render(request, 'projdetail.html', {'projects': proj_detail})


def albumview(request):
    albums = album.objects.all()
    return render(request, 'album.html', {'albums': albums})


def certview(request):
    certs = certifications.objects.all()
    return render(request, 'certs.html', {'certs': certs})


def Coursesview(request):
    courses = Courses.objects.all()
    semesters = Semester.objects.all()
    return render(request, 'courses.html', {'courses': courses,'semesters':semesters})
