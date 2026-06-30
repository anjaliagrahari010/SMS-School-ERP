from django.shortcuts import render, redirect
from user.models import *
from django.core.files.storage import FileSystemStorage
import datetime
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def teacherdash(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            sub_count=Subject.objects.filter(classid=teacher.tclass).count()
            stu_count=Student.objects.filter(sclass=teacher.tclass).count()
            return render(request,"teacherdash.html",locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)   
def teacherlogout(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            del request.session['teacher']
            return redirect('login')
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True) 
def teachersubjects(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            sub=Subject.objects.filter(teacherid=teacher.id)
          
            return render(request,"teachersubjects.html",locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True) 
def teacherattend(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            students=Student.objects.filter(sclass=teacher.tclass)
            att=StudentAttendence.objects.filter(sclass=teacher.tclass)
            if request.method=="POST":
                studentid=request.POST['studentid']
                studentname=request.POST['studentname']
                sclass=request.POST['sclass']
                d=datetime.datetime.today()
                date=d.strftime("%Y-%m-%d")
                status=request.POST['status']
                stu=StudentAttendence(studentid=studentid,studentname=studentname,sclass=sclass,date=date,status=status)
                stu.save()
                return redirect('teacherapp:teacherattend')
            return render(request,"teacherattend.html",locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)    
def teacherprofile(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            if request.method=="POST":
                pic=request.FILES['pic']
                fs=FileSystemStorage()
                filename=fs.save(pic.name,pic)
                teacher.pic=filename
                teacher.save()
                return redirect('teacherapp:teacherprofile')
            return render(request,"teacherprofile.html",locals())
    except:
        return redirect('login')