from django.urls import path
from . import views

urlpatterns = [
    path('new', views.index, name="index.html"),
    path('sum',views.add,name='add'),
    path('ne', views.average, name="average.html"),
    path('av', views.ave, name='avresult.html')

]