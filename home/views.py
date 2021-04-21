from django.shortcuts import render,HttpResponse
from home.models import Contact
from home.models import detail
from django.views.decorators.csrf import csrf_exempt
import razorpay


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
    return render(request,'status.html')
    #return HttpResponse("This is single PAge")
def plan(request):
    if request.method == "POST":
        amount = 5
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_c3TFXGS6EeIt7c','44lYMuRV7iEihEHGNLKd4PMP'))

        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture':'1' })

    return render(request,'plan.html')

def contacts(request):
    return render(request,'contact.html')
def payme(request):
    if request.method == "POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        phone=request.POST.get("phone")
        det=detail(firstname=firstname,lastname=lastname,phone=phone)
        det.save()
        amount = 5
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_c3TFXGS6EeIt7c', '44lYMuRV7iEihEHGNLKd4PMP'))
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture':'1' })

           # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)



    return render(request,'payme.html')

@csrf_exempt
def suce(request):
    return render(request,'suce.html')



