from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin),
    path('signup', views.signup),
    path('result', views.result),
]
