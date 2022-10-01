from django.shortcuts import render
from django.views import View
from django.views.generic import *
from django.http import HttpResponseRedirect
from project.models import *
from myuser.models import *
from donate.models import *
from comment.models import *
from rate.models import *
from reportcomment.models import *
from reportproject.models import *

from django.core.files.storage import FileSystemStorage

# Create your views here.

def projectdisplay(req,id):
    if req.session.get("email") is None:
        return HttpResponseRedirect('/login/')
    else:
        myaccount = Users.objects.filter(Email=req.session['email'])
        projdata = project.objects.get(id=id)
        projcom = comment.objects.filter(project_obj=projdata,on_comment=None)
        projdon = donate.objects.filter(project_obj=projdata)
        projtags = project_tags.objects.filter(project_obj=projdata)
        projpic = project_pic.objects.filter(project_obj=projdata)
        projrate = rate.objects.filter(project_obj=projdata)
        checkreply = comment.objects.filter(project_obj=projdata).exclude(on_comment=None)
        projreport= reportproject.objects.filter(project_obj=projdata)
        recommandproj = []
        for i in projtags:
            tagitems = project_tags.objects.filter(tag=i.tag)
            for j in tagitems:
                already = True
                if j.project_obj.id == projdata.id:
                    already = False
                for k in recommandproj:
                    if j.project_obj.id == k.project_obj.id :
                        already = False
                        break
                if already:
                    recommandproj.append(j)

            if len(recommandproj) >= 4:
                break

        rating_value=0.0
        for i in projrate:
            rating_value += i.rate_value


        donamount=0.0
        for i in projdon:
            donamount += i.amount
        if rating_value != 0 :
            rating_value = rating_value / len(projrate)

        #print(checkreply[0].comment_message)
        if req.method == 'GET':
            print(projdata.title)
            context={
                "currentuser": myaccount[0],
                "project_obj":projdata,
                "project_com": projcom,
                "project_rate": projrate,
                "project_don": projdon,
                "project_pics": projpic,
                "project_tags": projtags,
                "project_rep": checkreply,
                "project_recommand": recommandproj,
                "project_report": projreport,
                "totalrate": rating_value,
                "totaldon":donamount,

            }
            return render(req, 'project/simple.html',context)

        else:
            if req.POST['formname'] == "donform":
                currentuser = Users.objects.filter(Email=req.session.get('email'))
                donate.objects.create(myuser_obj=currentuser[0],project_obj=projdata,amount=req.POST['amountofdon'])
                newview = "/project/"+id
                return HttpResponseRedirect(newview)

            if req.POST['formname'] == "rateform":
                currentuser = Users.objects.filter(Email=req.session.get('email'))
                rate.objects.create(myuser_obj=currentuser[0],project_obj=projdata,rate_value=req.POST['rate'])
                newview = "/project/"+id
                return HttpResponseRedirect(newview)

            if req.POST['formname'] == "comform":
                currentuser = Users.objects.filter(Email=req.session.get('email'))
                comment.objects.create(myuser_obj=currentuser[0],project_obj=projdata,comment_message=req.POST['com_message'])
                newview = "/project/"+id
                return HttpResponseRedirect(newview)

            if req.POST['formname'] == "repform":
                currentuser = Users.objects.filter(Email=req.session.get('email'))
                oncom = comment.objects.get(id=req.POST['id'])
                comment.objects.create(myuser_obj=currentuser[0],project_obj=projdata,comment_message=req.POST['com_message'],on_comment=oncom)
                newview = "/project/"+id
                return HttpResponseRedirect(newview)

            if req.POST['formname'] == "reportcomform":
                currentuser = Users.objects.filter(Email=req.session.get('email'))
                oncom = comment.objects.get(id=req.POST['id'])
                reportcomment.objects.create(myuser_obj=currentuser[0],comment_obj=oncom,report_message=req.POST['report_message'])
                newview = "/project/"+id
                return HttpResponseRedirect(newview)

            if req.POST['formname'] == "reportprojform":
                currentuser = Users.objects.filter(Email=req.session.get('email'))
                reportproject.objects.create(myuser_obj=currentuser[0],project_obj=projdata,report_message=req.POST['report_message'])
                newview = "/project/"+id
                return HttpResponseRedirect(newview)

            return render(req, 'project/projectshow.html')


def createproject(req):
    if req.session.get('email') is None:
        return HttpResponseRedirect('/login/')
    else:
        if req.method == 'GET':
            allcat = category.objects.all()
            context={"proj_cat": allcat}
            return render(req, 'project/createproject.html',context)
        else:
            c=1
            picname="image"+str(c)
            while req.FILES.get(picname) != None:
                print(picname)
                c=c+1
                picname = "image" + str(c)

            t = 1
            tagname = "tag" + str(t)
            while req.POST.get(tagname) != None:
                print(tagname)
                t = t + 1
                tagname = "tag" + str(t)

            currentuser = Users.objects.filter(Email=req.session['email'])
            currentcat = category.objects.filter(name=req.POST['cat'])
            newproj = project.objects.create(title=req.POST['title'],details=req.POST['details'],target=req.POST['target'],poster=req.FILES['poster'],startdate=req.POST['startdate'],enddate=req.POST['enddate'],createdby=currentuser[0],cat=currentcat[0])

            i=1
            while i < c:
                print("in while images")
                picname = "image" + str(i)
                curpic = project_pic.objects.create(project_obj=newproj,picture=req.FILES[picname])
                print(curpic.picture.url)
                i=i+1

            i = 1
            while i < t:
                 tagname = "tag" + str(i)
                 curntag = project_tags.objects.create(project_obj=newproj, tag=req.POST[tagname])
                 print(curntag.tag)
                 i = i + 1

            return HttpResponseRedirect('/home/')


def homepage(req):
    if req.session.get('email') is None:
        return render(req, 'Login.html', {'error' : 'Please Enter Valid Data'})  
    else:
        wholeproj = project.objects.all()
        wholecat = category.objects.all()
        newwholecat = []
        for i in wholeproj:
            if i.cat.name not in newwholecat:
                newwholecat.append(i.cat.name)

        for i in newwholecat:
            print(i)

        allcat = category.objects.all()
        currentuser = Users.objects.filter(Email=req.session['email'])
        context = {
            "allproj" : wholeproj ,
            "allcat": newwholecat,
            "curuser": currentuser[0],
            "cat": allcat,
        }
        if req.method == 'GET':
            return render(req, "project/newtesthome.html", context)
        else:
            return HttpResponseRedirect('/tag/'+req.POST['tag'])



def editproject(req,id):
    if req.session.get("email") is None:
        return HttpResponseRedirect('/login/')
    else:
        if project.objects.get(id=id).createdby.Email != req.session['email']:
            return HttpResponseRedirect('/home/')
        else:
            projdata = project.objects.get(id=id)
            allcat = category.objects.all()
            projtags = project_tags.objects.filter(project_obj=projdata)
            projpic = project_pic.objects.filter(project_obj=projdata)
            projdon = donate.objects.filter(project_obj=projdata)

            donamount = 0.0
            for i in projdon:
                donamount += i.amount
            prentof = 1 / 4 * projdata.target

            if req.method == 'GET':

                context = {
                    "proj": projdata,
                    "tag": projtags,
                    "pic": projpic,
                    "proj_cat":allcat,
                    "totaldon": donamount,
                    "checkvalue": prentof,
                }
                return render(req, "project/editproject.html", context)
            else:
                if req.POST['formname'] == 'posterform':
                    projdata.poster.delete()
                    request_file = req.FILES['image']
                    fs = FileSystemStorage()
                    file = fs.save(request_file.name, request_file)
                    project.objects.filter(id=id).update(poster=file)
                elif req.POST['formname'] == 'basicinfo':
                    newcat = category.objects.filter(name=req.POST['cat'])
                    project.objects.filter(id=id).update(title=req.POST['title'],details=req.POST['details'],target=req.POST['target'],enddate=req.POST['enddate'],startdate=req.POST['startdate'],cat=newcat[0])
                elif req.POST['formname'] == 'tagremove':
                     project_tags.objects.filter(tag_id=req.POST['id']).delete()
                elif req.POST['formname'] == 'savetag':
                    t = 1
                    tagname = "tag" + str(t)
                    while req.POST.get(tagname) != None:
                        print(tagname)
                        t = t + 1
                        tagname = "tag" + str(t)
                    i =1
                    while i < t:
                        tagname = "tag" + str(i)
                        curntag = project_tags.objects.create(project_obj=projdata, tag=req.POST[tagname])
                        print(curntag.tag)
                        i = i + 1
                elif req.POST['formname'] == 'picremove':
                     project_pic.objects.filter(pic_id=req.POST['id'])[0].picture.delete()
                     project_pic.objects.filter(pic_id=req.POST['id']).delete()
                elif req.POST['formname'] == 'savepic':
                    print("enter saving images state ")
                    c = 1
                    picname = "image" + str(c)
                    while req.FILES.get(picname) != None:
                        print(picname)
                        c = c + 1
                        picname = "image" + str(c)
                    print("printing c value :" ,c)
                    i = 1
                    while i < c:
                        print("in while images")
                        picname = "image" + str(i)
                        curpic = project_pic.objects.create(project_obj=projdata, picture=req.FILES[picname])
                        print(curpic.picture.url)
                        i = i + 1
                return HttpResponseRedirect('/editing/'+id)



def searchbycat (req,name):
    if req.session.get('email') is None:
        return HttpResponseRedirect('/login/')
    else:
        currentcat = category.objects.filter(name=name)
        catprojects = project.objects.filter(cat=currentcat[0])
        context ={
            "allproj": catprojects,
        }
        if req.method == 'GET':
            return render(req,'project/search.html',context)
        else:
            return HttpResponseRedirect('/cat/'+name)

def searchbytag (req,name):
    if req.session.get('email') is None:
        return HttpResponseRedirect('/login/')
    else:
        tagproject = project_tags.objects.filter(tag="#"+name)
        torun = []
        for i in tagproject:
            torun.append(i.project_obj)
        context ={
            "allproj": torun
        }
        if req.method == 'GET':
            return render(req,'project/search.html',context)
        else:
            return HttpResponseRedirect('/tag/'+name)

def deleteproj(req,id):
    if req.session.get('email') is None:
        return HttpResponseRedirect('/login/')
    else:
        curproject = project.objects.get(id=id)
        projimages = project_pic.objects.filter(project_obj=curproject)
        for i in projimages:
            i.picture.delete()
        curproject.poster.delete()
        project.objects.filter(id=id).delete()
        return HttpResponseRedirect('/profile/')

def topproject(req):
    if req.session.get('email') is None:
        return HttpResponseRedirect('/login/')
    else:
        getallproj = project.objects.all()
        allproj =[]
        allrate = []
        for i in getallproj:
            getrate = rate.objects.filter(project_obj=i)
            totalrate=0
            for j in getrate:
                totalrate += j.rate_value
            if totalrate!=0:
                allproj.append(i)
                allrate.append(totalrate)

        max =-1
        proj_index=-1
        newratelist=[]
        newprojlist=[]
        for i in range(0,len(allrate)):
            for j in range(i+1,len(allrate)):
                if max < allrate[j]:
                    max = allrate[j]
                    allrate[j] = allrate[i]
                    allrate[i] = max
                    temp = allproj[j]
                    allproj[j] = allproj[i]
                    allproj[i] = temp
            if i == 5:
                break


        context = {
            "allproj": allproj[:6],
        }

        return render(req, 'project/search.html', context)

