from django.contrib import messages 
from django.shortcuts import render,redirect   
from django.contrib.auth.decorators import login_required
from app.models import Course, CustomUser,Session_Year,Trainee,Mentor,Feees
from django.contrib.auth.models import User

@login_required(login_url='/')
def HOME(request):
    return render(request,'manager/home.html')

def PROFILE(request):
    return render(request,'profile.html')




#####____TRAINEE___#######

@login_required(login_url='/')
def ADD_TRAINEE(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
    
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken')
            return redirect('add_trainee')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken')
            return redirect('add_trainee')
        
        else:
             user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
             )

             user.set_password(password)
             user.save()

             course = Course.objects.get(id=course_id)
             print(course_id)

             session_year = Session_Year.objects.get(id=session_year_id)

             print("hiiiii :",type(session_year))

             trainee = Trainee(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
             )
             trainee.save()
             messages.success(request, " Trainee Successfully Added !")
             return redirect('add_trainee')

    context = {
        'course':course,
        'session_year':session_year,
    }

   
    return render(request,'manager/add_trainee.html',context)

@login_required(login_url='/')
def VIEW_TRAINEE(request):
    trainee =Trainee.objects.all()
    context= {
        'trainee': trainee,
    }
    return render(request,'manager/view_trainee.html',context)

@login_required(login_url='/')
def EDIT_TRAINEE(request,id):
    trainee=Trainee.objects.filter(id=id)

    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    
    context = {
        'trainee': trainee,
        'course':course,
        'session_year':session_year,


    }

    return render(request,'manager/edit_trainee.html',context)

@login_required(login_url='/')
def UPDATE_TRAINEE(request):
    if request.method=="POST":
        trainee_id=request.POST.get('trainee_id')
        profile_pic=request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

   

    return render (request,'manager/edit_trainee.html')

@login_required(login_url='/')
def DELETE_TRAINEE(request,admin):
    # t_admin = admin
    trainee=CustomUser.objects.get(id=admin)
    trainee.delete()
    messages.success(request,'Record is successfully deleted')
    return redirect('view_trainee')
    

#######__MENTOR___########


@login_required(login_url='/')
def ADD_MENTOR(request):
    
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
          
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken')
            return redirect('add_mentor')
        elif CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken')
            return redirect('add_mentor')
        
        else:
             user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
             )

             user.set_password(password)
             user.save()

          
             user.save()
             

    
        mentor = Mentor(
            admin=user,
            address = address,
            gender= gender
        )
        mentor.save()
        messages.success(request, " Mentor Successfully Added !")
        return redirect('add_mentor')
    

   
    return render(request,'manager/add_mentor.html')

@login_required(login_url='/')
def VIEW_MENTOR(request):
    mentor =Mentor.objects.all()
    context= {
        'mentor': mentor,
    }
    return render(request,'manager/view_mentor.html',context)

@login_required(login_url='/')
def EDIT_MENTOR(request,id):
    trainee=Trainee.objects.filter(id=id)

    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    
    context = {
        'trainee': trainee,
        'course':course,
        'session_year':session_year,
    }

    return render(request,'manager/edit_mentor.html',context)

@login_required(login_url='/')
def UPDATE_MENTOR(request):
    if request.method=="POST":
        trainee_id=request.POST.get('trainee_id')
        profile_pic=request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')


    return render (request,'manager/edit_mentor.html')

@login_required(login_url='/')
def DELETE_MENTOR(request,id):
    mentor=Mentor.objects.get(id=id)    
    print(mentor)
    mentor.delete()
    messages.success(request,'Record is successfully deleted')
    return redirect('view_mentor')
    
#####____COURSE____#####


@login_required(login_url='/')
def ADD_COURSE(request):

    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course=Course(
            name = course_name, 
        )
        course.save()
        messages.success(request,'Course added successfully')
        return redirect('add_course')
    
    return render(request,'manager/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'manager/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course=Course.objects.get(id=id)

    context ={
        'course':course
    }
    return render(request,'manager/edit_course.html',context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    return render(request,'manager/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course_id = id
    course=Course.objects.get(id=id)
    course.delete()
    messages.success(request,'Record is successfully deleted')
    return redirect('view_course')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_start=request.POST.get('session_start')
        session_end= request.POST.get('session_end')
        session_name = request.POST.get('session_name')

        session=Session_Year(
            session_start=session_start,
            session_end=session_end,
            session_name=session_name,
        )
        session.save()
        messages.success(request,'session are successfully added')
        return redirect('add_session')

    return render(request,'manager/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session=Session_Year.objects.all()

    context={
        'session':session
    }
    return render(request,'manager/view_session.html',context)


@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session_id = id
    session=Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request,'Record is successfully deleted')
    return redirect('view_session')

@login_required(login_url='/')
def VIEW_FEES(request):
    feees = Feees.objects.all()
    context = {
        'feees':feees,
    }
    return render(request,'manager/view_feees.html',context)

@login_required(login_url='/')
def DELETE_FEES(request,id):
    fees_id = id
    fees=Feees.objects.get(id=id)
    fees.delete()
    messages.success(request,'Record is successfully deleted')
    return redirect('view_fees')
