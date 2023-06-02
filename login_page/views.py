from datetime import timedelta, datetime
import time

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib import messages
from . import models
from django.contrib.auth.decorators import login_required


rec_idd = 0
job_idd = 0
app_idd = 0


def landing_page(request):
    return render(request, 'login_page/landing_page.html')


def a_signup(request):
    # User.objects.create_user()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #         messages.success(request, f'Your account has been created. You can log in now!')
    #         return redirect('/a_login')
    # else:
    #     form = UserCreationForm()
    #
    # context = {'form': form}
    # return render(request, 'login_page/a_signup.html', context)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            alert = True
            return render(request, "login_page/a_signup.html", {'alert2': alert})

        # user = User.objects.create_user(username=name, email=email, password=password)
        applicant = Applicant.objects.create(username=name, email=email, password=password, name=name)
        # user.save()
        applicant.save()
        global app_idd
        app_idd = applicant.id
        alert = True
        context = {
            "alert": alert,
            "applicant_id": app_idd
        }
        return render(request, "login_page/a_signup.html", context)
    return render(request, "login_page/a_signup.html")


def r_signup(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #         messages.success(request, f'Your account has been created. You can log in now!')
    #         return redirect('/r_login')
    # else:
    #     form = UserCreationForm()
    #
    # context = {'form': form}
    # return render(request, 'login_page/r_signup.html', context)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        company = request.POST['company']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            alert = True
            context = {
                "alert2": alert,
            }
            return render(request, "login_page/r_signup.html", context)

        # user = User.objects.create_user(username=name, email=email, password=password)
        recruiter = Recruiter.objects.create(username=name, email=email, password=password, name=name, company=company)
        # user.save()
        recruiter.save()
        alert = True
        global rec_idd
        rec_idd = recruiter.id
        context = {
            "alert": alert,
            "recruiter_id": rec_idd
        }
        return render(request, "login_page/r_signup.html", context)
    return render(request, "login_page/r_signup.html")


def a_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        applicants = Applicant.objects.all()
        for i in applicants:
            if i.email == email and i.password == password:
                alert = True
                global app_idd
                app_idd = i.id
                jobs_to_show = Job.objects.all()
                context = {
                    "alert": alert,
                    "applicant_id": app_idd,
                    "job_posts": jobs_to_show
                }
                return render(request, "login_page/a_login.html", context)
        alert = True
        return render(request, "login_page/a_login.html", {'alert2': alert})
        # user = authenticate(username=email, password=password)
        #
        # if user is not None:
        #     login(request, user)
        #     if request.user.is_superuser:
        #         return HttpResponse("You are not an applicant!!")
        #     else:
        #         return redirect("/all job posts")
        # else:
        #     alert = True
        #     return render(request, "login_page/all_job_posts.html", {'alert': alert})
    return render(request, 'login_page/a_login.html')


def r_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        recruiters = Recruiter.objects.all()
        alert = True
        for i in recruiters:
            if i.email == email and i.password == password:
                global rec_idd
                rec_idd = i.id
                jobs = Job.objects.all()
                jobs_to_show = []
                for j in jobs:
                    if j.recruiter_id == rec_idd:
                        jobs_to_show.append(j)
                context = {
                    "alert": alert,
                    "recruiter_id": rec_idd,
                    "job_posts": jobs_to_show
                }
                return render(request, "login_page/r_login.html", context)
        return render(request, "login_page/r_login.html", {'alert2': alert})
    # if request.method == "POST":
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(username=email, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         if request.user.is_sushellperuser:
    #             return HttpResponse("You are not an applicant!!")
    #         else:
    #             return redirect("/all_job_posts")
    #     else:
    #         alert = True
    #         return render(request, "login_page/r_posted_jobs.html", {'alert': alert})
    return render(request, 'login_page/r_login.html')


# @login_required(login_url='/a_login')
def all_job_posts(request):
    global job_idd
    alert = True
    if request.method == "POST":
        if "job_id" in request.POST:
            job_id = request.POST['job_id']
            print(job_id + "all_job_posts")
            job_idd = int(job_id)
            applicant_id = request.POST['applicant_id']
            context = {'applicant_id': applicant_id,
                       'job_id': job_id,
                       "alert": alert,
                       }
            jobs = Job.objects.all()
            jobs_applied_to = JobsAppliedTo.objects.all()
            jobs_applied = [i.job_id for i in jobs_applied_to if i.applicant_id == applicant_id]
            jobs_to_show = []
            for i in jobs:
                if i.id in jobs_applied:
                    continue
                else:
                    jobs_to_show.append(i)
            for i in range(len(jobs_to_show)):
                if job_id == jobs_to_show[i].id:
                    jobs_to_show.pop(i)
                    break
            context["job_posts"] = jobs_to_show
            return render(request, "login_page/all_job_posts.html", context)

    context = {}
    jobs = Job.objects.all()
    context["job_posts"] = jobs
    return render(request, 'login_page/all_job_posts.html', context)


# @login_required(login_url='/a_login')
def a_job_apply(request):
    alert = True
    if request.method == "POST":
        job_id = request.POST['job_id']
        print(job_id + "a_apply_job")
        applicant_id = request.POST['applicant_id']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        jobs_to_show = request.POST['jobs_to_show']
        context = {
            'job_posts': jobs_to_show,
            'alert': alert,
        }
        job_applied = JobsAppliedTo.objects.create(name=name, email=email, job_id=int(job_id), message=message, applicant_id=applicant_id)
        job_applied.save()
        return render(request, "login_page/a_apply_job.html", context)
    return render(request, "login_page/a_job_apply.html")


# @login_required(login_url='/a_login')
# def applied(request):
#
#     jobs = JobsAppliedTo.objects.all()
#     for i in jobs:
#
#     context = {'my_url': 'login_page/job post page.html'}
#     return render(request, 'login_page/applied.html', context)


# @login_required(login_url='/r_login')
def r_write_job(request):
    global rec_idd
    alert = True
    if request.method == "POST":
        name = request.POST['name']
        rep = request.POST['rep']
        skills = request.POST['skills']
        date_posted = str(date.today())
        time_posted = str(datetime.now())[11:-7]
        job = Job.objects.create(name=name, rep=rep, skills=skills, date_posted=date_posted, time_posted=time_posted, recruiter_id=rec_idd)
        job.save()
        context = {
            "name": name,
            "skills": skills,
            "rep": rep,
            "date_posted": date_posted,
            "time_posted": time_posted,
            "alert": alert
        }
        return render(request, "login_page/r_write_job.html", context)
    return render(request, 'login_page/r_write_job.html')


# @login_required(login_url='/r_login')
def r_posted_jobs(request):
    global rec_idd
    alert = True
    if request.method == "POST":
        job_id = request.POST["job_id"]
        print(job_id)
        print(type(job_id))
        if "delete" in request.POST:
            Job.objects.filter(id=int(job_id)).delete()
            jobs_to_show = []
            jobs = Job.objects.all()
            for i in jobs:
                if i.recruiter_id == rec_idd:
                    jobs_to_show.append(i)
            context = {
                "job_id": job_id,
                "job_posts": jobs_to_show,
                "alert": alert
            }
            return render(request, "login_page/r_posted_jobs.html", context)
        else:
            job = Job.objects.get(id=int(job_id))
            print(job)
            jobs_applied_to = JobsAppliedTo.objects.all()
            applicants = []
            for i in jobs_applied_to:
                if i.job_id == int(job_id):
                    applicants.append(i)
            context = {
                "job_id": job_id,
                "applicants": applicants,
                "job": job,
                "alert2": alert
            }
            return render(request, "login_page/r_posted_jobs.html", context)
    jobs_to_show = []
    jobs = Job.objects.all()
    for i in jobs:
        if i.recruiter_id == rec_idd:
            jobs_to_show.append(i)
    context = {
        "job_posts": jobs_to_show
    }
    return render(request, "login_page/r_posted_jobs.html", context)


# @login_required(login_url='/r_login')
def r_see_all_applicants(request, job_id):
    # global rec_idd
    applicants_to_show = JobsAppliedTo.objects.filter(job_id=int(job_id))
    job = Job.objects.filter(id=int(job_id))[0]
    print(type(job))
    alert = True
    #job_id = request.GET['job_id']
    #jobs_applied_to = JobsAppliedTo.objects.all()
    #applicants_to_show = []
    #for i in jobs_applied_to:
        #if i.job_id == int(job_id):
            #applicants_to_show.append(i)

    context = {
        # "recruiter_id": rec_idd,
        "job_id": job_id,
        "applicants_to_show": applicants_to_show,
        "alert": alert,
        "job": job,
    }
    return render(request, "login_page/r_see_all_applicants.html", context)


def log_out(request):
    global rec_idd
    global job_idd
    global app_idd
    rec_idd = 0
    job_idd = 0
    app_idd = 0
    logout(request)
    return redirect("/")


def about(request):
    return render(request, 'login_page/about.html')


def contact(request):
    return render(request, 'login_page/contact.html')
