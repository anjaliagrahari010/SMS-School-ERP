from django.shortcuts import render,redirect,reverse
from .models import LoginUser, Enquiry
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request, 'index.html')
def vision(request):
    return render(request, 'vision.html')  
def school(request):
    return render(request, 'school.html') 
def founder(request):
    return render(request, 'founder.html')
def login(request):
    return render(request, 'login.html')
def chairman(request):
    return render(request, 'chairman.html')
def principal(request):
    return render(request, 'principal.html')
def SMT(request):
    return render(request, 'SMT.html')

def academic(request):
    return render(request, 'academic.html')

def transport(request):
    return render(request, 'transport.html')

def medical(request):
    return render(request, 'medical.html')

def smart_class(request):
    return render(request, 'smart_class.html')

def admission_procedure(request):
    return render(request, 'admission.html')

def prospectus(request):
    return render(request, 'prospectus.html')

def rules(request):
    return render(request, 'rules.html')

def fee(request):
    return render(request, 'fee.html')

def career(request):
    return render(request, 'career.html')


def media(request):
    return render(request, 'media_news.html')

def video(request):
    return render(request, 'media_video.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']
        d = datetime.datetime.today()
        enquiry_date = d.strftime("%d-%m-%Y %I:%M %p" )
        enq = Enquiry(name = name, mobile = mobile, email = email, message = message, enquiry_date = enquiry_date)
        enq.save()
        return render(request,'index.html', {'msg':"Your Enquiry is submitted"})
    return render(request, 'contact.html')


# def apply(request):
#     if request.method=="POST":
#         name = request.POST['name']
#         post = request.POST['post']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         city = request.POST['city']
#         doc = 
#         d = datetime.datetime.today()
#         enquiry_date = d.strftime("%d-%m-%Y %I:%M %p" )
#         enq = Enquiry(name = name, mobile = mobile, email = email, area = area, enquiry_date = enquiry_date)
#         enq.save()
#         return render(request,'index.html', {'msg':"Your Enquiry is submitted"})
#     return render(request, 'contact.html')

def logcode(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        usertype = request.POST['utype']
        try:
            user = LoginUser.objects.get(username=username, password = password, usertype=usertype)
            if user.usertype=="admin":
                request.session['username']=username
                return redirect('adminapp:dash')
            elif user.usertype=="student":
                request.session['student']=username
                return redirect('studentapp:studentdash')
            elif user.usertype == "teacher":
                request.session['teacher'] = username
                return redirect('teacherapp:teacherdash')
        except:
            return redirect('login')


