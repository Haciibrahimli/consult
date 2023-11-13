from django.urls import path
from my_app.views import *

urlpatterns = [

path('service/',service_view,name = 'service'),
path('detail/<slug>/',detail_view,name = 'detail'),

]
