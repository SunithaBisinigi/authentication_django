from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing,name='landing'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('home/signout/', views.signout, name='signout'),
    path('home/',views.home,name='home'),
    path('mem/',views.mem,name='mem'),
]
