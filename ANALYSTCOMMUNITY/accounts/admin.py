from django.contrib import admin
from accounts.models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('phone_number','password','user_name','last_name','user_profile_image','user_email','user_post','user_designation','user_bio')


admin.site.register(CustomUser,CustomUserAdmin)