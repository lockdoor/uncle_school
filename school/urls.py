from django.urls import path, include
from .views import homepage, about, contactus, showscore
app_name = 'school'
urlpatterns = [    
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contactus/', contactus, name='contactus'),
    path('showscore/', showscore, name='showscore'),
]