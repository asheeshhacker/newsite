from django.urls import path
from . import views
urlpatterns = [
    path('',views.sub1,name='sub1'),
]