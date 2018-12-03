from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Speaker,session,Visitor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import *
from django.core.mail import send_mail
import pdb
import datetime
# Create your views here.
def index(request):
    return render(request,'app/index.html')
def signup(request):
    if request.method=='GET':
        return render(request,"app/register.html")
    elif request.method=='POST':
        # bio=request.POST['bio']
        # twitter=request.POST["twitter"]
        # facebook=request.POST["facebook"]
        try:
            fname=request.POST['firstName']
            lname=request.POST['lastName']
            # pic=request.FILES.get('profile_pic')
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            newusr=auth.models.User.objects.create_user(username,email,password)
            newusr.first_name=fname
            newusr.last_name=lname
            Speaker.objects.get_or_create(speaker=newusr)
            return render(request,"app/success.html")
        except Exception as e:
            context={'WARNING':e,}
            return render(request,"app/register.html",context)
def login(request):
    if request.method == "GET":
        return render(request,'app/login.html')
    elif request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password'];
        user=auth.authenticate(username=username,password=password)
        speaker=user
        if user is not None:
            if  user.is_active:
                speaker=auth.login(request,user);
                next="";
                if 'next' in request.GET:
                    next=request.GET["next"]
                    print(next)
                if next == None or next=="":
                    next="/"
                    print(next)
                return redirect(next)
            else:
                return render(request,"app/login.html",{'WARNING':"your account is disabled"})
        else:
            return render(request,"app/login.html",{'WARNING':"invalid user or password"})
def logout(request):
    auth.logout(request)
    return render(request,"app/index.html")
@login_required
def session_create(request):
    if request.method=="GET":
        return render(request,"app/create_session.html")
    elif request.method=="POST":
        try:
            title=request.POST["title"]
            abstract=request.POST["abstract"]
            speaker=request.POST["speaker"]
            venue=request.POST["venue"]
            update_time=request.POST["update_time"]
            created=datetime.datetime.now()
            speaker=request.POST["speaker"]
            spkr=User.objects.get(username=speaker)
            session_speaker=Speaker.objects.get(speaker=spkr)
            session.objects.create(title=title,abstract=abstract,speaker=session_speaker,venue=venue,session_date=update_time,created=created).save()
            return render(request,"app/registered.html")
        except Exception as e:
            return render(request,"app/create_session.html",{'WARNING':'there are some errors in fields'})
@login_required
def SessionUpdate(request,session_id):
    if request.method=="GET":
        sessions=session.objects.get(pk=session_id)
        return render(request,"app/session_update.html",{"session":sessions})
    elif request.method=="POST":
        try:
            title=request.POST["title"]
            abstract=request.POST["abstract"]
            venue=request.POST["venue"]
            update_time=request.POST["update_time"]
            session.objects.filter(pk=session_id).update(title=title,abstract=abstract,venue=venue,session_date=update_time)
            return render(request,"app/registered.html")
        except Exception as e:
            sessions=session.objects.get(pk=session_id)
            return render(request,"app/session_update.html",{"WARNING":e})
class SessionDelete(LoginRequiredMixin,DeleteView):
    model=session
    success_url=reverse_lazy('app:session_list')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class SessionDetail(DetailView):
    model=session
class SessionList(ListView):
    session_list= session.objects.order_by('created')[:5]
    model=session
    template_name="app/session_list.html"
def interested(request,session_id):
    sessions=session.objects.get(pk=session_id)
    try:
        goings=session.objects.filter(pk=session_id).get(pk=session_id)
        goings.going+=1
        goings.save()
        return HttpResponseRedirect(reverse('app:session_detail', args=(session_id,)))
    except Exception as e:
        sessions=session.objects.get(pk=session_id)
        return render(request,"app/session_update.html",{"WARNING":e})
def contact(request):
    if request.method=="GET":
        return render(request,"app/contact.html")
    elif request.method=="POST":
        try:
            email=request.POST["Email"]
            name=request.POST["Name"]
            msg=request.POST["Msg"]
            Visitor.objects.create( V_name=name,
                                    V_email=email,
                                    V_message=msg)
            return render(request,"app/contact.html")
        except Exception as e:
            return render(request,"app/registered.html",{"WARNING":e})
