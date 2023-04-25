
import statistics
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import mentor_views, views,trainee_views,manager_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/",views.BASE,name="base"),
   
    ###__login urls____###
    
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    ###___PROFILE_UPDATE___###

    path('manager/profile',manager_views.PROFILE,name='profile'),
    path('mentor/profile',mentor_views.PROFILE,name='profile'),

    #manager urls
    path('manager/Home',manager_views.HOME, name='manager_Home'),

    #Mentor urls
     path('mentor/Home',mentor_views.HOME, name='mentor_Home'),


    ###___TRAINEE___###

    path('manager/trainee/add',manager_views.ADD_TRAINEE, name='add_trainee'),
    path('manager/trainee/view',manager_views.VIEW_TRAINEE, name='view_trainee'),
    path('manager/trainee/edit/<str:id>',manager_views.EDIT_TRAINEE, name='edit_trainee'),
    path('manager/trainee/update',manager_views.UPDATE_TRAINEE, name='update_trainee'),
    path('manager/trainee/delete/<str:admin>',manager_views.DELETE_TRAINEE, name='delete_trainee'), 

    ###____MENTOR___###

    path('manager/mentor/add',manager_views.ADD_MENTOR, name='add_mentor'),
    path('manager/mentor/view',manager_views.VIEW_MENTOR, name='view_mentor'),
    path('manager/mentor/edit/ ',manager_views.EDIT_MENTOR, name='edit_mentor'),
    path('manager/mentor/update',manager_views.UPDATE_MENTOR, name='update_mentor'),
    path('manager/mentor/delete/<str:id>',manager_views.DELETE_MENTOR, name='delete_mentor'),

    ###___COURSE___###

    path('manager/course/add',manager_views.ADD_COURSE, name='add_course'),
    path('manager/course/view',manager_views.VIEW_COURSE, name='view_course'),
    path('manager/course/edit/<str:id>',manager_views.EDIT_COURSE, name='edit_course'),
    path('manager/course/delete/<str:id>',manager_views.DELETE_COURSE, name='delete_course'),
    
   
    ###___SESSION___###
    path('manager/session/add',manager_views.ADD_SESSION, name='add_session'),
    path('manager/session/view',manager_views.VIEW_SESSION, name='view_session'),
    path('manager/session/delete/<str:id>',manager_views.DELETE_SESSION, name='delete_session'),
   

    ##FEEDBACK
    path('mentor/Feedback',mentor_views.MENTOR_FEEDBACK, name='mentor_feedback'),
     path('mentor/Feedback/save',mentor_views.MENTOR_FEEDBACK_SAVE, name='mentor_feedback_save'),
   

    ##FEESPAY
    path('index1',trainee_views.home,name='home'),
    path('success',trainee_views.SUCCESS,name='success'),
    path('manager/feees/view',manager_views.VIEW_FEES, name='view_fees'),
    path('manager/feees/delete/<str:id>',manager_views.DELETE_FEES, name='delete_feees'),
    


    #FORGOTPASSWORD
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),      
    path("password_reset", views.password_reset_request, name="password_reset"),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


