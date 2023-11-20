from django.urls import path
from account.views import *


urlpatterns = [
    path("register/", register_view, name='register'),
    path("activate/<slug>/", activate_view, name='activate'),
]