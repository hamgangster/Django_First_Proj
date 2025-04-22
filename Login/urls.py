from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='signup'),
    path('login',views.Login,name='Login'),
    path('home/',include('Home.urls')),
    path('logout/',views.logout,name='logout')
]
