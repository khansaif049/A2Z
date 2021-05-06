from home.forms import StaFrom
from django.shortcuts import render,HttpResponse
from home.models import Contact
from home.models import detail
from home.models import Conr
from home.models import Sta


from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages




def home(request):
    
    return render(request,'home.html')


# Create your views here.
def index(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        times=request.POST.get("times")
        address=request.POST.get("address")
        Rail=request.POST.get("Rail")
        station=request.POST.get("station")
        locality=request.POST.get("locality")
        work=request.POST.get("work")
        contact=Contact(name=name, email=email,phone=phone,address=address,Rail=Rail,times=times,station=station,locality=locality,work=work)
        contact.save()
        









    return render(request,'main.html')
    # return HttpResponse("This is Home PAge")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is About PAge")
def projects(request):
    return render(request,'projects.html')

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is service PAge")


    # return HttpResponse("This is contact PAge")

def single(request):
    
    
    if request.method=="POST":
        
        
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            sta=Sta(email=email,phone=phone)
            sta.save()
        
    return render(request, 'status.html')
        
        
    

   

    
    #return HttpResponse("This is single PAge")
def plan(request):

    if request.method == "POST":
        amount = 5
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_c3TFXGS6EeIt7c','44lYMuRV7iEihEHGNLKd4PMP'))

        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture':'1' })

    return render(request,'plan.html')

def contacts(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        email=request.POST.get("email")
        add=request.POST.get("add")
        conr=Conr(fname=fname,email=email,add=add)
        conr.save()


    return render(request,'contact.html')
@csrf_exempt

def payme(request):
    if request.method == "POST":
        
        razorpay_payment_id=request.POST.get("razorpay_payment_id")
        det=detail(razorpay_payment_id=razorpay_payment_id)
        det.save()
        amount = 5
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_c3TFXGS6EeIt7c', '44lYMuRV7iEihEHGNLKd4PMP'))
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture':'1' })

           # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)



    return render(request,'payme.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'invalid_data' in request.session.keys():
            request.session.pop('invalid_data', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/plan")

        else:
            request.session['invalid_data'] = True
            return render(request, "login1.html", {'invalid_data':True})
    else:
        if request.user.is_authenticated:
            return redirect("/main")
        else:
            return render(request, "login1.html")

    

  

def regi(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if 'invalid_username' in request.session.keys():
            request.session.pop('invalid_username', False)
        if 'invalid_email' in request.session.keys():
            request.session.pop('invalid_email', False)
        if User.objects.filter(username=username).exists():
            request.session['invalid_username'] = True
            return render(request, "regi.html", {'invalid_username':True})
        elif User.objects.filter(email=email).exists():
            request.session['invalid_email'] = True
            return render(request, "regi.html", {'invalid_email':True})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect("/main")

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/main")
        else:
            return render(request, "regi.html")
    



    




def logout(request):
    django_logout(request)
    return render(request, "login1.html")


@csrf_exempt
def suce(request):
    return render(request,'suce.html')







