from django.urls import path
#from .import views 
from project.views import TestView

urlpatterns = [
    path('get/', TestView.as_view(), name='test'),
]