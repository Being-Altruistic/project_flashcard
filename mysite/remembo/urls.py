from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('createcard', views.createcard, name="createcard"),
    path('P<question_id>[0-9]+', views.detail, name="detail"),
    path('search', views.search, name="search"),
    path('viewbookmarks', views.viewbookmarks, name="viewbookmarks"),
    path('studypage', views.studypage, name="studypage"),
]
app_name = 'remembo'

