from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from twilio.rest import Client
import random
# Create your views here.
def first(request):
    abc= Tableform(request.POST)
    if request.method== 'POST':
        if abc.is_valid():
            abc.save()
        return redirect(login)
    return render(request, 'firstpage.html',{'form':abc})


def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
    return render(request, 'display.html', {'hotel_images': Hotels})


def second(request):
    abc= Table.objects.all()
    return render(request, 'secondpage.html', {'abc':abc})

def delete(request, id):
    abc = Table.objects.get(id=id)
    abc.delete()
    return redirect(second)



def edit(request,id):
    xyz = Table.objects.get(id=id)
    abc = Tableform(request.POST or None, instance=xyz)
    if request.method== 'POST':
        if abc.is_valid():
            abc.save()
        return redirect(second)
    return render(request, 'firstpage.html', {'form': abc})





def login(request):
    msg=""
    if request.method == 'POST':
        a = request.POST.get('email')
        b = request.POST.get('pswd')
        try:
            abc = Table.objects.get(email=a, password=b)
            if abc is not None:
                return redirect(second)
        except:
            msg= "Invalid User"
    return render(request, 'login.html', {'msg': msg})


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'image.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')

def mob(request):
    body = ""

    otp = random.randint(1000, 9999)

    request.session['otp'] = otp

    print(otp)
    a = "************************"
    b = "***********************"
    abc= Client(a,b)

    if request.method == 'POST':
        mob = request.POST.get('mob')
        abc.messages.create(from_="(205) 512-6494", to = mob, body="Hi your verification code is - " + str(otp))
        return redirect(otp_view)
    return render(request, 'otp1.html',{'msg':otp})

def otp_view(request):
    otp_got = request.session['otp']
    if request.method == 'POST':
        abc= request.POST.get('mob')
        abc= int(abc)
        if abc == otp_got:
            return render(request, 'firstpage.html')
    return render(request, 'otp2.html')