
from django.shortcuts import render,redirect   
from django.contrib.auth.decorators import login_required
from app.models import Feees
import razorpay

from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/')
def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))
        
        client=razorpay.Client(auth=("rzp_test_UjtjOMFyusGmZb","o72VT36ruDm71CYLW1u52tx5"))
        payment= client.order.create({'amount':amount*100, 'currency':'INR','payment_capture':1 })

        print(payment)
        feees=Feees(
            name=name,
            amount=amount,
            payment_id=payment['id']
        )
        feees.save()
        return render(request,"pay/index1.html",{'payment':payment})
    else:
        return render(request,"pay/index1.html")


    # return render(request,"pay/index1.html")

@csrf_exempt
def SUCCESS(request):
    if request.method=="POST":
        a=request.POST
    return render(request,"pay/success.html")