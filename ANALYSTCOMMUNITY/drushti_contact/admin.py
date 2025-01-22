from django.contrib import admin
from drushti_contact.models import userContact
from drushti_contact.models import My_Contact



# Register your models here.
class userContactAdmin(admin.ModelAdmin):
    list_display=('name','email','contact_message')


admin.site.register(userContact,userContactAdmin)


class My_ContactAdmin(admin.ModelAdmin):
    list_display=('cont_title','cont_meg','my_location','location_des','my_phone','my_phone1','my_email','my_email1','cont_btn')


admin.site.register(My_Contact ,My_ContactAdmin)