from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

from adOfRoommate.models import AdOfRoommate
from adOfHouse.models import AdOfHouse


def adRoommate_new(request):
    if request.user.is_authenticated:
        print(request.user)
    else:
        return HttpResponse('Login First')

    if request.method == 'POST':
        priceMax = request.POST.get('priceMax')
        priceMin = request.POST.get('priceMin')
        u1 = User.objects.get(username=request.user.username)

        personalInfo = request.POST.get('personalInfo')

        adOfRoommate = AdOfRoommate.objects.create(priceMax=priceMax, priceMin=priceMin, user1=u1, personalInfo=personalInfo)
        adOfRoommate.save()

        adOfRoommate = AdOfRoommate.objects.all().order_by('date_publish').reverse()
        adOfHouse = AdOfHouse.objects.all().order_by('date_publish').reverse()
        context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
        return render(request, 'index.html', context)

    else:
        return render(request, 'HouseAdvertisement.html', {})



def adRoommateRender(request):
    adOfRoommate = AdOfRoommate.objects.all().order_by('date_publish').reverse()
    adOfHouse = AdOfHouse.objects.all().order_by('date_publish').reverse()
    context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
    return render(request, 'index.html', context)
