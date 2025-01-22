from django.contrib import admin
from my_drushtiserplans.models import ServicesPlans
from my_drushtiserplans.models import PlanDescription
# Register your models here.

class ServicesPlansAdmin(admin.ModelAdmin):
    list_display=('Suggestion_title','Plan_title','Plan_amount','Plan_highlight1','Plan_highlight2','Plan_highlight3','Plan_highlight4','Plan_highlight5','Plan_btn')

admin.site.register(ServicesPlans, ServicesPlansAdmin)

class PlanDescriptionAdmin(admin.ModelAdmin):
    list_display=('Plan_des_title','Plan_Condition1','Plan_Condition2','Plan_Condition3','Plan_Condition4','Plan_Condition5')

admin.site.register(PlanDescription, PlanDescriptionAdmin)