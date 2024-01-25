
from django.urls import path

from . import views
app_name='bankapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('getdata/',views.getdata,name='getdata'),
    path('adddata/',views.adddata,name='adddata')
]
