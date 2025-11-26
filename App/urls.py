from django.urls import path
from . import views

urlpatterns=[
    path('',views.information,name='information'),
    path('download-challenge/', views.download_challenge_file, name='download_challenge'),

]