from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="some string")
    email = models.CharField(max_length=50, default="some string")
    username = models.CharField(max_length=50, default="some string")
    password = models.CharField(max_length=50, default="some string")

    def __str__(self):
        return str(self.name)


class Recruiter(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="some string")
    company = models.CharField(max_length=50, default="some string")
    email = models.CharField(max_length=50, default="some string")
    username = models.CharField(max_length=50, default="some string")
    password = models.CharField(max_length=50, default="some string")

    def __str__(self):
        return str(self.name)


class Job(models.Model):
    # STATUS = (
    #     (0, 'normal'),
    #     (-1, 'deleted'),
    # )
    recruiter_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200, default="some string")
    skills = models.CharField(max_length=1000, default="some string")
    rep = models.CharField(max_length=1000, default="some string")
    date_posted = models.CharField(max_length=20, default="some string")
    time_posted = models.CharField(max_length=20, default="some string")
    # status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return str(self.name)


class JobsAppliedTo(models.Model):
    job_id = models.IntegerField(default=0)
    applicant_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="some")
    email = models.CharField(max_length=50, default="some")
    message = models.CharField(max_length=2000, default="some")

