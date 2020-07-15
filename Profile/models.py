from django.db import models


# Create your models here.
class Semester(models.Model):
    Semester = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.Semester


class Courses(models.Model):
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    ClassName = models.CharField("Class Name", null=False, max_length=20)
    Description = models.TextField(null=False, max_length=50)
    Professor = models.TextField(null=True, max_length=30)
    Grade = models.CharField(null=False, max_length=5)

    def __str__(self):
        return self.ClassName + " - " + self.Description + " - " + self.Grade


class Job(models.Model):
    jobs = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/')
    job_description = models.TextField("Job Description", max_length=500)
    startDate = models.DateField("Start Date")
    End_Date = models.DateField("End Date")
    employer = models.TextField(max_length=100)
    contact_info = models.EmailField(max_length=30)

    def __str__(self):
        return self.jobs + " - " + self.employer + " - " + self.contact_info


class Projects(models.Model):
    Name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)
    startDate = models.DateField("Start Date")
    End_Date = models.DateField("End Date")
    Mentor = models.TextField(max_length=100)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.Name + " - " + self.Mentor + " - " + self.email


class album(models.Model):
    Name = models.TextField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.Name


class certifications(models.Model):
    Status_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'), ]

    CertName = models.TextField(max_length=50)
    Issued_By = models.TextField(max_length=25)
    Status = models.CharField(max_length=11, choices=Status_CHOICES)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.CertName + " - " + self.Issued_By + " - " + self.Status
