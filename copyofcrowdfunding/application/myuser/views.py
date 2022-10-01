from django.shortcuts import render
from django.views import View
from django.views.generic import *
from django.http import HttpResponseRedirect
from myuser.models import *
from project.models import *
from donate.models import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render 
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate,login , logout
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import login

# Create your views here.

def getstarted(request):
    return render(request, 'getstarted.html')


def registertaionForm(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST, request.FILES)
        if form.is_valid():
            email = request.POST['Email']
            username = request.POST['First_Name']
            form.save()
            email_subject = 'Activate Your Account'
            email_body = f'Welcome {username}'
            from_email = settings.EMAIL_HOST_USER
            recipient = [email]
            # send_mail(
            #     email_subject,
            #     email_body,
            #     from_email,
            #     recipient,
            #     fail_silently=False
            # )
            html_content = render_to_string("email_template.html",{'title' : email_subject, 'content' : email_body})
            text_content = strip_tags(html_content)

            Email = EmailMultiAlternatives(
                email_subject,
                text_content,
                from_email,
                recipient
            )
            Email.attach_alternative(html_content,"text/html")
            Email.send()
        else:
            allcontext= {'rf' : RegisterationForm, 'error' : 'Please Enter Valid Data'}
            return render(request, 'Registeration.html', context=allcontext )
    

    return render(request, 'Registeration.html', {'rf' : RegisterationForm})


def loginForm(request):
    if(request.session.get('email') is None):
        if (request.method == 'GET'):
            return render(request, 'Login.html')
        else:
            userobject = Users.objects.filter(Email=request.POST['email'], Password=request.POST['password'])
            if (len(userobject) > 0):
                request.session['email'] = userobject[0].Email
                return HttpResponseRedirect('/home/')
            else:
                return render(request, 'Login.html', {'error' : 'Invalid Email or Password'})
    else:
        return HttpResponseRedirect('/home/')


def logoutview(request):
    request.session.clear()
    logout(request)
    return render(request, "getstarted.html")

def myuserprofile(req):
    if req.session.get('email') is None:
        return HttpResponseRedirect('/login/')
    else:
        curuser = Users.objects.filter(Email=req.session['email'])
        myproj =  project.objects.filter(createdby=curuser[0])
        mydonate = donate.objects.filter(myuser_obj=curuser[0])
        if req.method == 'GET':
            context = {
                'myinfo': curuser[0],
                'myproject' : myproj,
                'mydonation' : mydonate
            }
            return render(req,'myuser/profile.html',context)
        else:
            if req.POST['formname'] == 'basicinfo':
                Users.objects.filter(Email=req.session['email']).update(fname=req.POST['fname'], lname=req.POST['lname'],password=req.POST['password'],phonenumber=req.POST['phonenumber'])
            elif req.POST['formname'] == 'profilepic':
                if req.FILES.get('image') != None :
                    curuser[0].Profile_Picture.delete()
                    request_file=req.FILES.get('image')
                    fs = FileSystemStorage()
                    file = fs.save(request_file.name,request_file)
                    Users.objects.filter(Email=req.session['email']).update(Profile_Picture=file)
            elif req.POST['formname'] == 'mydon':
                if req.POST['opertype'] == 'edit':
                    donate.objects.filter(id=req.POST['id']).update(amount=req.POST['newvalue'])
                else:
                    donate.objects.filter(id=req.POST['id']).delete()
            return HttpResponseRedirect('/profile/')