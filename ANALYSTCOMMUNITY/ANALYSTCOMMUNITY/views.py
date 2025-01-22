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
from home.models import ourClient
from myanalyst.models import Analyst
from usr_profile.models import *
from store.models import *
from usr_profile.forms import ProfileFrom
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

@login_required()
def drushti_home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    servicesData=Analytics.objects.all()
    faqData=FAQ.objects.all()
    clientData=ourClient.objects.all()
    data={
        'servicesData':servicesData,
        'faqData':faqData,
        'clientData':clientData,
        'cartItems':cartItems,
    }
    return render(request, 'drushtihome.html',data)


def drushtiservices(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    servicesData=Analytics.objects.all()
    data={
        'servicesData':servicesData,
        'cartItems':cartItems,
    }
    return render(request, 'services.html',data)


def about_drushti(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    return render(request, 'aboutdrushti.html',{'cartItems':cartItems})

def contact_drushti(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    contactData=My_Contact.objects.all()
    cont_data={
        'contactData':contactData,
        'cartItems':cartItems
    }
    return render(request, 'contactdrushti.html',cont_data)

def feedback_drushti(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    
    return render(request, 'drushtifeedback.html',{'cartItems':cartItems})
        

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
        return redirect('home')
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
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

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
    return render(request, 'drushtilogin.html',{'cartItems':cartItems})

def logoutUser(request):
    logout(request)
    return redirect('userSignIn')

def servicesplans_drushti(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    keyData=ServicesPlans.objects.all()
    tryme={
        'keyData' :keyData,
        'cartItems':cartItems,
    }
    return render(request, 'ourplans.html',tryme)

def plan_des_drushti(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    planData=PlanDescription.objects.all()
    BigData={
        'planData' :planData,
        'cartItems':cartItems,
    }
    return render(request, 'PlanDescription.html',BigData)

def userProfile(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    return render(request,'myprofilehome.html',{'cartItems':cartItems})

def profile(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if request.method =='POST': 
        form=ProfileFrom(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            user_name=request.user.user_name
            return redirect('profile/')
            
    else:
        form=ProfileFrom(instance=request.user.profile)
    context={'form':form, 'cartItems':cartItems}
    return render(request, 'profile.html',context)


@login_required
def dashboard(request):
    if Analyst.objects.filter(user=request.user).exists():
        return redirect('analystdash')  
    else:
        return redirect('dash')


def privacyPolicy(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    return render(request, 'policy.html',{'cartItems':cartItems})















