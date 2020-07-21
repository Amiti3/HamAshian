from django.shortcuts import render, redirect
from adOfHouse.models import *
from adOfRoommate.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout



def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        global user
        user = User.objects.create(username = username , email = email)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        return HttpResponse('welcome ' + username)
    else:
        return render(request, 'SignUp.html', {})


def user_login(request):
    global user
    print('*********************')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('advertisement')
            else:
                message = "Your account was inactive."
                print(message)
                return render(request, 'SignIn .html', {})
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(username,password))
            message = "Invalid login details given"
            return render(request, 'SignIn .html', {'message':message})
    else:
        return render(request, 'SignIn .html', {})


def user_logout(request):
    logout(request)
    global user
    user = None
    return HttpResponse('logged out')


def chooseOne(request):
    return render(request, 'Advertisement.html', {})

def index(request):
    adOfRoommate = AdOfRoommate.objects.all().order_by('date_publish').reverse()
    adOfHouse = AdOfHouse.objects.all().order_by('date_publish').reverse()
    context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
    return render(request, 'index.html', context)


def sortNew(request):
    adOfRoommate = AdOfRoommate.objects.all().order_by('date_publish').reverse()
    adOfHouse = AdOfHouse.objects.all().order_by('date_publish').reverse()
    context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
    return render(request, 'index.html', context)

def sortOld(request):
    adOfRoommate = AdOfRoommate.objects.all().order_by('date_publish')
    adOfHouse = AdOfHouse.objects.all().order_by('date_publish')
    context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
    return render(request, 'index.html', context)

def sortExpensive(request):
    adOfRoommate = AdOfRoommate.objects.all().order_by('priceMax').reverse()
    adOfHouse = AdOfHouse.objects.all().order_by('price').reverse()
    context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
    return render(request, 'index.html', context)

def sortCheap(request):
    adOfRoommate = AdOfRoommate.objects.all().order_by('priceMax')
    adOfHouse = AdOfHouse.objects.all().order_by('price')
    context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
    return render(request, 'index.html', context)

def aboutUs(request):
    return render(request, 'InfoPages/aboutUs.html')

def ad_making(request):
    return render(request, 'InfoPages/ad_making.html')

def contactUs(request):
    return render(request, 'InfoPages/contactUs.html')

def rules(request):
    return render(request, 'InfoPages/rules.html')

# def myprofile(request):
#     if request.user.is_authenticated:
#         u1 = User.objects.get(username=request.user.username)
#         return render(request, 'Profile.html', {'user':u1})
#
#     return HttpResponse('Something went wrong')

def viewAdHouse(request, id):
    if request.user.is_authenticated:
        print(request.user)
    else:
        return HttpResponse('Login First')
    # reqFrom = str(request)[str(request).find('/')+1:str(request).rfind('/')]
    adOfHouse = AdOfHouse.objects.get(id = id)
    u1 = adOfHouse.user1
    context = {'user': u1, 'ad': adOfHouse}
    return render(request, 'Profile.html', context)

def viewAdRoommate(request, id):
    if request.user.is_authenticated:
        print(request.user)
    else:
        return HttpResponse('Login First')
    # reqFrom = str(request)[str(request).find('/')+1:str(request).rfind('/')]
    adOfRoommate = AdOfRoommate.objects.get(id = id)
    u1 = adOfRoommate.user1
    context = {'user': u1, 'ad': adOfRoommate}
    return render(request, 'Profile1.html', context)

def inout(request):
    if request.user.is_authenticated:
        logout(request)
        global user
        user = None
        return HttpResponse('logged out')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            return HttpResponse('welcome ' + username)
        else:
            return render(request, 'SignUp.html', {})

def search(request):
    if request.method == 'POST':
        city = request.POST.get('search')
        adOfHouse = AdOfHouse.objects.get(city = city)
        adOfRoommate = AdOfRoommate.objects.get(city = city)
        context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
        return render(request, 'index.html', context)
    else:
        return HttpResponse('somthing went wrong!')