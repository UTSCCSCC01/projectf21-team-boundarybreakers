from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators import csrf
from .models import customer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here.
@csrf_exempt
def customer_profile(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'did not recieve a POST request'}, status=403)
    oldusername = request.POST.get('username')
    oldpassword = request.POST.get('password')
    if customer.objects.filter(username=oldusername,password=oldpassword):
        #username and password is verified so changes can be made now
        c=customer.objects.get(username=oldusername,password=oldpassword)
        newusername = request.POST.get('newusername')
        newpassword = request.POST.get('newpassword')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        c.username=newusername
        c.password=newpassword
        c.email=email
        c.firstname=firstname
        c.lastname=lastname
        c.save()
        return JsonResponse({'status': 'success'}, status=200)
    else: 
        return JsonResponse({'status': 'username/password incorrect'}, status=400)