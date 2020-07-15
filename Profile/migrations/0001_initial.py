# Generated by Django 3.0.8 on 2020-07-14 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CertName', models.TextField(max_length=50)),
                ('Issued_By', models.TextField(max_length=25)),
                ('Status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=11)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobs', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('job_description', models.TextField(max_length=500, verbose_name='Job Description')),
                ('startDate', models.DateField(verbose_name='Start Date')),
                ('End_Date', models.DateField(verbose_name='End Date')),
                ('employer', models.TextField(max_length=100)),
                ('contact_info', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=500)),
                ('startDate', models.DateField(verbose_name='Start Date')),
                ('End_Date', models.DateField(verbose_name='End Date')),
                ('Mentor', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassName', models.CharField(max_length=20, verbose_name='Class Name')),
                ('Description', models.TextField(max_length=50)),
                ('Professor', models.TextField(max_length=30, null=True)),
                ('Grade', models.CharField(max_length=5)),
                ('Semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Semester')),
            ],
        ),
    ]
