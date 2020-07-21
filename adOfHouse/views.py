from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from house.models import House
from adOfHouse.models import AdOfHouse
from adOfRoommate.models import AdOfRoommate



def adHouse_new(request):
    if request.user.is_authenticated:
        print(request.user)
    else:
        return HttpResponse('Login First')

    if request.method == 'POST':
        price = request.POST.get('price')
        u1 = User.objects.get(username=request.user.username)

        city = request.POST.get('city')
        region = request.POST.get('region')
        address = request.POST.get('address')
        houseArea = request.POST.get('houseArea')
        roommmateNum = request.POST.get('roommmateNum')
        roomNum = request.POST.get('roomNum')
        wcNum = request.POST.get('wcNum')
        ageOfHouse = request.POST.get('ageOfHouse')

        h1 = House.objects.create(city=city, region=region, address=address, houseArea=houseArea, roommmateNum=roommmateNum,
                                  roomNum=roomNum, wcNum=wcNum, ageOfHouse=ageOfHouse)
        h1.save()
        personalInfo = request.POST.get('personalInfo')

        adOfHouse = AdOfHouse.objects.create(price=price, user1=u1, house1=h1, personalInfo=personalInfo)
        adOfHouse.save()

        adOfRoommate = AdOfRoommate.objects.all().order_by('date_publish').reverse()
        adOfHouse = AdOfHouse.objects.all().order_by('date_publish').reverse()
        context = {'adOfHouse': adOfHouse, 'adOfRoommate': adOfRoommate}
        return render(request, 'index.html', context)

    else:
        return render(request, 'RommateAdvertisement.html', {})


def adHouseRender(request):
    adOfHouse = AdOfHouse.objects.all().order_by('date_publish').reverse()
    print(adOfHouse)
    return render(request, 'index.html', {'ads': adOfHouse})
