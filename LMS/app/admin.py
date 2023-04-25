from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display=['id','username','user_type']

class MentorModel(admin.ModelAdmin):
    list_display=['id']


admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Trainee)
admin.site.register(Mentor_Feedback)
admin.site.register(Feees)

