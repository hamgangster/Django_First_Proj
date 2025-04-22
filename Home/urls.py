from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='Main'),
    path('about',views.About,name='About'),
    path('shop/',include('Shop.urls'))
]
