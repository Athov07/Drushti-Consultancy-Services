"""
URL configuration for ANALYSTCOMMUNITY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ANALYSTCOMMUNITY import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('',include('candidate.urls')),
    path('',include('myanalyst.urls')),
    path('explore/', views.explore_drushti, name='explore'),
    path('home/', views.drushti_home, name='home'),
    path('home/userLogIn/', views.drushti_home, name='home'),
    path('about/', views.about_drushti, name='about'),
    path('home/about/', views.about_drushti, name='about'),
    path('home/userLogIn/about/', views.about_drushti, name='about'),
    path('services/', views.drushtiservices, name='services'),
    path('contact/', views.contact_drushti, name='contact'),
    path('save_Contact/', views.saveContact, name='save_Contact'),
    path('userLogIn/', views.my_LogIn, name='userLogIn'),
    path('userSignIn/', views.UserSignIn, name='userSignIn'),
    # path('userLogIn/userSignIn/', views.UserSignIn, name='userLogIn'),
    path('userLogIn/analystSignIn/', views.AnalystSignIn, name='analystSignIn'),
    path('analystSignIn/', views.AnalystSignIn, name='analystSignIn'),
    path('logout/',views.logoutUser,name='logout'),
    path('servicesplans/', views.servicesplans_drushti, name='servicesplans'),
    path('servicesplans/plansDes/', views.servicesplans_drushti, name='servicesplans'),
    path('plansDes/', views.plan_des_drushti, name='plansDes'),
    path('plansDes/servicesplans/', views.plan_des_drushti, name='plansDes'),
    path('feedback/', views.feedback_drushti, name='feedback'),
    path('save_Feed/', views.saveFeedback, name='save_Feed'),
    path('profile/', views.userProfile, name='profile'),
    # path('profile/myprofile/', views.userProfile, name='profile'),
    path('myprofile/profile/', views.userProfile, name='profile'),
    path('myprofile/', views.profile, name='myprofile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('policy/', views.privacyPolicy, name='policy'),
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    