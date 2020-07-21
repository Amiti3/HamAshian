from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    # path('', ArticleList.as_view(), name = 'article_list'),
    # path('/<int:id>', article_id),
    path('/new', views.adRoommate_new, name='adRoommate_new'),
    path('', views.adRoommateRender, name='adRoommateRender'),
]