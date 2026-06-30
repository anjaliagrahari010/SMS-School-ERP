from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    
    path('', views.index, name = "index"),
    path('vision-mission', views.vision, name = "vision"),
    path('about-school', views.school, name = "school"),
    path('founder-message', views.founder, name = "founder"),
    path('login-sms', views.login, name = "login"),
    path('chairman-message', views.chairman, name = "chairman"),
    path('principals-message', views.principal, name = "principal"),
    path('school-management-team', views.SMT, name = "SMT"),
    path('logcode', views.logcode, name="logcode"),
    path('academics', views.academic, name = "academic"),
    path('transport', views.transport, name = "transport"),
    path('medical-room', views.medical, name="medical"),
    path('smart-class', views.smart_class, name="smart_class"),
    path('admission-procedure', views.admission_procedure, name="admission"),
    path('download-prospectus', views.prospectus, name = "prospectus"),
    path('rules-regulation', views.rules, name="rules"),
    path('fee-structure', views.fee, name="fee"),
    path('career', views.career, name = "career"),
    path('media_news', views.media, name = "media_news"),
    path('media_video', views.video, name="media_video"),
    path('contact-us', views.contact, name="contact"),

    



]
