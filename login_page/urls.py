from django.urls import path

from . import views


urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("a_signup/", views.a_signup, name="a_signup"),
    path("r_signup/", views.r_signup, name="r_signup"),
    path("a_login/", views.a_login, name="a_login"),
    path("r_login/", views.r_login, name="r_login"),
    path("all_job_posts/", views.all_job_posts, name="all_job_posts"),
    path("a_job_apply/", views.a_job_apply, name="a_job_apply"),
    path("r_write_job/", views.r_write_job, name="r_write_job"),
    path("r_posted_jobs/", views.r_posted_jobs, name="r_posted_jobs"),
    # path("r_see_all_applicants/", views.r_see_all_applicants, name="r_see_all_applicants"),
    path("r_see_all_applicants/<int:job_id>/", views.r_see_all_applicants, name="r_see_all_applicants"),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
