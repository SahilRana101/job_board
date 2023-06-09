# Generated by Django 4.1.5 on 2023-05-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200)),
                ('job_description', models.CharField(max_length=1000)),
                ('applications_count', models.IntegerField(default=0)),
                ('job_posted_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ApplicantSignUpDetails',
        ),
        migrations.DeleteModel(
            name='JobPost',
        ),
        migrations.DeleteModel(
            name='RecruiterSignUpDetails',
        ),
    ]
