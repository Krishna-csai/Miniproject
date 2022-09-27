from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ,name="home"),
    path('search', views.search, name="searchpage ") ,
    path('search/<code>/', views.searchpage , name='search'),
    path('codes', views.codes, name='codes'),
    path('codesfunction', views.codesfunction , name='codesfunction'),
    path('credits/' , views.credits , name='credits'),
]