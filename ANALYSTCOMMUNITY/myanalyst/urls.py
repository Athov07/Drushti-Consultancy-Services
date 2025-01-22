from django.urls import path
from .import views
urlpatterns = [
    path('analystdash/',views.AnalystHome,name='analystdash'),
    path('candidatedetails/<int:id>/',views.AnalystCandidateDetails,name='candidatedetails'),
    path('postjob/',views.postJobs,name='postjob'),
    path('acceptapplication/',views.acceptApplication,name='acceptapplication')    
]
