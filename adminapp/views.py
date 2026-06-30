from django.shortcuts import render,redirect,reverse
import datetime
from user.models import *
from django.views.decorators.cache import cache_control
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def index(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            stu_count=Student.objects.all().count()
            t_count=Teacher.objects.all().count()
            cl_count=Class.objects.all().count()
            return render(request, 'adminhome.html',locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def teacher(request):
    try: 
        if request.session['username']!=None:
            adminid=request.session['username']
            t=Teacher.objects.all()
            cl=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                number=request.POST['number']
                email=request.POST['email']
                qua=request.POST['qua']
                exp=request.POST['exp']
                tsalary=request.POST['tsalary']
                tclass=request.POST['tclass']
                address=request.POST['address']
                password=request.POST['password']
                created=datetime.datetime.today()
                try:
                    obj=LoginUser.objects.get(username=email)
                    if obj is not None:
                        msg="Email address is already taken"
                        return render(request,'teacher.html',{'msg':msg,'t':t,'cl':cl})
                except ObjectDoesNotExist:
                    teacher=Teacher(name=name,number=number,email=email,qua=qua,exp=exp,tsalary=tsalary,tclass=tclass,address=address,created=created)
                    teacher.save()
                    log=LoginUser(username=email,password=password,usertype="teacher")
                    log.save()
                    t=Teacher.objects.all()
                    cl=Class.objects.all()
                    return render(request,'teacher.html',{'msg':"Teacher is Added",'t':t,'cl':cl})
            return render(request, 'teacher.html',locals())
    except:
        return redirect('login')

@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def student(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            stu=Student.objects.all()
            cl=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                mobile=request.POST['mobile']
                email=request.POST['email']
                fnumber=request.POST['fnumber']
                dob=request.POST['dob']
                sclass=request.POST['sclass']
                sfee=request.POST['sfee']
                balance=request.POST['balance']
                address=request.POST['address']
                password=request.POST['password']
                try:
                    obj=LoginUser.objects.get(username=email)
                    if obj is not None:
                        msg="Email address is already taken"
                        return render(request,'student.html',{'msg':msg,'stu':stu,'cl':cl,'msg':msg})
                except ObjectDoesNotExist:
                    stu=Student(
                        name=name,
                        fname=fname,
                        mobile=mobile,
                        email=email,
                        fnumber=fnumber,
                        dob=dob,
                        sclass=sclass,
                        sfee=sfee,
                        balance=balance,
                        address=address,
                    )
                    stu.save()
                    log=LoginUser(username=email,password=password,usertype="student")
                    log.save()
                    msg="Student is added successfully"
                    stu=Student.objects.all()
                    cl=Class.objects.all()
                    return render(request,'student.html',{'msg':msg,'stu':stu,'cl':cl})
            
            return render(request, 'student.html',locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def attendance(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            attend=StudentAttendence.objects.all()
            return render(request, 'attendance.html',locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def classes(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            c=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                roomno=request.POST['roomno']
                seats=request.POST['seats']
                c=Class(name=name,roomno=roomno,seats=seats)
                c.save()
                return redirect('adminapp:classes')
            return render(request, 'classes.html',locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def subjects(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            cl=Class.objects.all()
            sub=Subject.objects.all()
            teacher=Teacher.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                classid=request.POST['classid']
                teacherid=request.POST['teacherid']
                book=request.POST['book']
                s=Subject(name=name,classid=classid,teacherid=teacherid,book=book)
                s.save()
                return redirect('adminapp:subjects')
            return render(request, 'subjects.html',locals())
    except:
        return redirect('login')

@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def logout(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            del request.session['username']
            return redirect('login')
    except:
        return redirect('login')

def delteacher(request,id):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:teacher')
    except:
        return redirect('login')

def delclass(request,id):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            Class.objects.get(id=id).delete()
            return redirect('adminapp:classes')
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def edit(request,id):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            stu=Student.objects.get(id=id)
            cl=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                mobile=request.POST['mobile']
                email=request.POST['email']
                fnumber=request.POST['fnumber']
                dob=request.POST['dob']
                sclass=request.POST['sclass']
                sfee=request.POST['sfee']
                balance=request.POST['balance']
                address=request.POST['address']
                Student.objects.filter(id=id).update(name=name,fname=fname,mobile=mobile,email=email,fnumber=fnumber,dob=dob,sclass=sclass,sfee=sfee,balance=balance,address=address)
                return redirect('adminapp:student')
            return render(request,'edit.html',{'stu':stu,'cl':cl})
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)   
def delstudent(request,id):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            stu = Student.objects.get(id=id)
            stu.delete()
            return redirect('adminapp:student')
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)   
def edit_teacher(request, id):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            t = Teacher.objects.get(id=id)
            if request.method == "POST":
                name = request.POST['name']
                number = request.POST['number']
                email = request.POST['email']
                qua = request.POST['qua']
                exp = request.POST['exp']
                tsalary = request.POST['tsalary']
                tclass = request.POST['tclass']
                address = request.POST['address']
                Teacher.objects.filter(id=id).update(
                    name=name,
                    number = number,
                    qua = qua,
                    exp = exp, 
                    tsalary = tsalary, 
                    tclass = tclass, 
                    address = address, )
                return redirect ('adminapp:teacher', {'cl':cl})
            cl=Class.objects.all()
            return render(request,"edit_teacher.html", locals())
    except:
        return redirect('login')
    
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def editclass(request,id):
     try:
          if request.session['username']!=None:
               adminid=request.session['username']
               c=Class.objects.get(id=id)
               if request.method=="POST":
                    name=request.POST['name']
                    roomno=request.POST['roomno']
                    seats=request.POST['seats']
                    
                    Class.objects.filter(id=id).update(name=name,roomno=roomno,seats=seats)
                    return redirect('adminapp:classes')
               return render(request,"edit_class.html",{'c':c})
     except:
          return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def delsubject(request,id):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            sub = Subject.objects.get(id=id)
            sub.delete()
            return redirect('adminapp:subjects')
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewenquiries(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            enq=Enquiry.objects.all()
            return render(request, 'viewenquiries.html',locals())
    except:
        return redirect('login')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)   
def admincp(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                cpassword=request.POST['cpassword']
                try:
                    obj=LoginUser.objects.get(username=adminid,password=oldpassword)
                    if newpassword!=cpassword:
                        msg="Enter same password"
                        return render(request, 'admincp.html',locals())
                    elif oldpassword==obj.password:
                        LoginUser.objects.filter(username=adminid,password=oldpassword).update(password=newpassword)
                        return redirect('adminapp:logout')
                except:
                    return render(request,'admincp.html',{'msg':"Invalid Old Password"})
            return render(request, 'admincp.html',locals())
    except:
        return redirect('login')


# def viewcarapply(request):
#     try:
#         if request.session['username']!=None:
#             apply=Apply.objects.all()
#             return render(request, 'viewcarapply.html',locals())
#     except:
#         return redirect('login')

    
