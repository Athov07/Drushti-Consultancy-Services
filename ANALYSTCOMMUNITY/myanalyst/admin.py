from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Analyst)
admin.site.register(JobPost)
admin.site.register(CandidateApplications)
admin.site.register(SelectCandidateJob)