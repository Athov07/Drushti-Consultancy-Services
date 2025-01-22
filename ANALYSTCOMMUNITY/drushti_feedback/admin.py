from django.contrib import admin
from drushti_feedback.models import userFeedback
# Register your models here.
class userFeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','satisfied','rnumber','feed_message')


admin.site.register(userFeedback,userFeedbackAdmin)