from django.urls import path
from candidate import views
from .import views
urlpatterns = [
     path('dash/',views.candidateHome,name='dash'),
     path('applyPlan/<int:id>/',views.applyPlan,name='apply'),
     path('applylist/',views.myjoblist,name='applylist')
]
