from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
       (1,'Manager'),
        (2,'Mentor'),
        (3,'Trainee'),
    )

    username=models.CharField(max_length=20,unique=True,blank=True,null=True)
    email=models.EmailField(max_length=30,unique=True)
    user_type = models.CharField(choices=USER,max_length=50,default='Manager')
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']

class Course(models.Model):
    name=models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    name=models.CharField(max_length=50)
    session_start= models.DateTimeField(auto_now_add=True)
    session_end= models.DateTimeField(auto_now_add=True)
    session_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)

class Trainee(models.Model):
    admin =models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address= models.TextField()
    gender=models.CharField(max_length=50)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    session_year_id=models.ForeignKey(Session_Year,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + "  " + self.admin.last_name 


class Mentor(models.Model):
    
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
    

class Mentor_Feedback(models.Model):
    mentor_id=models.ForeignKey(Mentor,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mentor_id.admin.first_name + " " +self.mentor_id.admin.last_name

class Feees(models.Model):
    name= models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)