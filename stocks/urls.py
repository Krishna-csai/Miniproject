from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ,name="home"),
    path('search/', views.search, name="searchpage ") ,
    path('search/<code>/', views.searchpage , name='search'),
    path('codes/', views.codes, name='codes'),
    path('codesfunction', views.codesfunction , name='codesfunction'),
    path('gainers/', views.gainers , name='gainers'),
    path('gainersfunction1/', views.gainersfunction1, name='gainersfunction1'),
    path('gainersfunction2/', views.gainersfunction2, name='gainersfunction2'),
    path('gainersfunction3/', views.gainersfunction3, name='gainersfunction3'),
    path('losers/', views.losers , name='losers'),
    path('losersfunction1/', views.losersfunction1, name='losersfunction1'),
    path('losersfunction2/', views.losersfunction2, name='losersfunction2'),
    path('losersfunction3/', views.losersfunction3, name='losersfunction3'),
    path('predictions/', views.predictions, name='prediction'),
    path('about/', views.about, name='about'),
    path('members/', views.members, name='members'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contactus/', views.contactus, name='contactus'),
]