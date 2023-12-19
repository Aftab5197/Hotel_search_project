from django.urls import path

from home import views
from home.views import get_hotel

urlpatterns = [
    path('',views.home,name='home'),
    path('api/get-hotels/', get_hotel),
]