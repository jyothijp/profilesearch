from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
    #path('',views.upload_pdf,name='home'),
    path('', views.home, name='home'),
    #path('parser/', views.homepage, name='homepage'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('parser/',views.homepage, name='homepage'),
    #path('profile/',views.profile, name='profile'),
    #path('view', views.show_file, name="view"),
    #path('view', views.upload_pdf, name ="view"),
         ]