from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect
from home.models import Analytics
from drushti_feedback.models import userFeedback
from drushti_contact.models import userContact
from drushti_contact.models import My_Contact
from my_drushtiserplans.models import ServicesPlans
from my_drushtiserplans.models import PlanDescription
from explore_more.models import explore_more
from home.models import FAQ
from usr_profile.models import *
from usr_profile.forms import ProfileFrom
from myanalyst.models import Analyst
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User= get_user_model()





def explore_drushti(request):
    exploreData=explore_more.objects.all()
    temp={
        'exploreData':exploreData
    }
    return render(request, 'exploredrushti.html',temp)

def drushti_home(request):
    servicesData=Analytics.objects.all()
    faqData=FAQ.objects.all()
    data={
        'servicesData':servicesData,
        'faqData':faqData
    }
    return render(request, 'drushtihome.html',data)

def about_drushti(request):
    return render(request, 'aboutdrushti.html')

def contact_drushti(request):
    contactData=My_Contact.objects.all()
    cont_data={
        'contactData':contactData
    }
    return render(request, 'contactdrushti.html',cont_data)

def feedback_drushti(request):
     return render(request, 'drushtifeedback.html')
        

def saveFeedback(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        satisfied=request.POST.get('satisfy')
        rnumber=request.POST.get('rating')
        feed_message=request.POST.get('msg')
        my_feed=userFeedback(name=name,email=email,phone=phone,satisfied=satisfied,rnumber=rnumber,feed_message=feed_message)
        my_feed.save()
    return render(request, 'drushtifeedback.html')
 
def saveContact(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        email=request.POST.get('email')
        contact_message=request.POST.get('msg')
        my_cont=userContact(name=name,email=email,contact_message=contact_message)
        my_cont.save()
    return render(request, 'contactdrushti.html')

def UserSignIn(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password') 
        user_name=request.POST.get('user_name')
        last_name=request.POST.get('last_name')
        user_profile_image=request.POST.get('user_profile_image')
        user_email=request.POST.get('user_email')
        user_post=request.POST.get('user_post')
        user_bio=request.POST.get('user_bio')
        user=User.objects.create_user(phone_number=phone_number,password=password,user_name=user_name,last_name=last_name,user_profile_image=user_profile_image,user_email=user_email,user_post=user_post,user_bio=user_bio)
        login(request, user) 
        return redirect('dash')
    return render(request, 'drushtiSignIn.html')
        

def AnalystSignIn(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password') 
        user_name=request.POST.get('user_name')
        last_name=request.POST.get('last_name')
        user_profile_image=request.POST.get('user_profile_image')
        user_email=request.POST.get('user_email')
        user_post=request.POST.get('user_post')
        user_designation=request.POST.get('user_designation')
        user_bio=request.POST.get('user_bio')
        user=User.objects.create_user(phone_number=phone_number,password=password,user_name=user_name,last_name=last_name,user_profile_image=user_profile_image,user_email=user_email,user_post=user_post,user_designation=user_designation,user_bio=user_bio)
        Analyst(user=user).save()
        login(request, user)
        return redirect('analystdash')
    return render(request, 'analystSignIn.html')
        

def my_LogIn(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        user=authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            if Analyst.objects.filter(user=user).exists():
                return redirect('analystdash')
            return redirect('dash')
            # return HttpResponse("success")
        else:
            return HttpResponse("InValid Username or Password")
            # return 0
    return render(request, 'drushtilogin.html')

def logoutUser(request):
    logout(request)
    return redirect('userSignIn')

def servicesplans_drushti(request):
    keyData=ServicesPlans.objects.all()
    tryme={
        'keyData' :keyData
    }
    return render(request, 'ourplans.html',tryme)

def plan_des_drushti(request):
    planData=PlanDescription.objects.all()
    BigData={
        'planData' :planData
    }
    return render(request, 'PlanDescription.html',BigData)


def userProfile(request):
    return render(request,'myprofilehome.html')

def profile(request):
    if request.method =='POST': 
        form=ProfileFrom(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            user_name=request.user.user_name
            return redirect('profile/')
            
    else:
        form=ProfileFrom(instance=request.user.profile)
    context={'form':form}
    return render(request, 'profile.html',context)




def cart(request):
    return render(request, 'myprofilehome.html')
