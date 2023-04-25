from django.shortcuts import redirect,render
from django.contrib import messages 
from app.models import Course, CustomUser,Session_Year,Trainee,Mentor,Mentor_Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/')
def HOME(request):
    return render(request,'mentor/home.html')

def PROFILE(request):
    return render(request,'profile.html')

###____FEEDBACK___ ###

def MENTOR_FEEDBACK(request):
    mentor_id=Mentor.objects.get(admin=request.user.id)
    feedback_history=Mentor_Feedback.objects.filter(mentor_id=mentor_id)

    context={
        'feedback_history':feedback_history,
    }
    

    return render(request,'mentor/feedback.html',context)

def MENTOR_FEEDBACK_SAVE(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        mentor=Mentor.objects.get(admin=request.user.id)
        feedback=Mentor_Feedback(
            mentor_id=mentor,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()
    return redirect('mentor_feedback')






















