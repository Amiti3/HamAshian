from django.contrib import admin
from django.urls import path, include
from house.views import *





urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', user_login ,name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name= 'logout'),

    path('adOfHouse', include('adOfHouse.urls')),
    path('adOfRoommate', include('adOfRoommate.urls')),
    path('advertisement', chooseOne , name = 'advertisement'),
    path('', index, name='index'),

    path('index/sortNew', sortNew , name = 'sortNew'),
    path('index/sortOld', sortOld , name = 'sortOld'),
    path('index/sortExpensive', sortExpensive , name = 'sortExpensive'),
    path('index/sortCheap', sortCheap , name = 'sortCheap'),

    path('index/aboutUs', aboutUs , name = 'aboutUs'),
    path('index/ad_making', ad_making , name = 'ad_making'),
    path('index/contactUs', contactUs , name = 'contactUs'),
    path('index/rules', rules , name = 'rules'),

    # path('myprofile', myprofile, name='myprofile'),
    path('viewAdHouse/<int:id>', viewAdHouse, name='viewAdHouse'),
    path('viewAdRoommate/<int:id>', viewAdRoommate, name='viewAdRoommate'),

    path('inout', inout, name='inout'),

    path('search', search, name='search'),

]

