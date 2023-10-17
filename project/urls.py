from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from app import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing,name='landing'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('home/signout/', views.signout, name='signout'),
    path('home/',login_required(views.home),name='home'),
    path('mem/',views.mem,name='mem'),

    path('list/', views.todo_list, name='todo_list'),
    path('add_todo_item/', views.add_todo_item, name='add_todo_item'),
    path('complete/<int:item_id>/', views.complete_todo_item, name='complete_todo_item'),
    path('delete/<int:item_id>/', views.delete_todo_item, name='delete_todo_item'),


] 



#     path('react-app/', views.react_app, name='react_app'),
#     re_path(r'^.*', TemplateView.as_view(template_name='index.html'), name='react-app'),
# ]
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#     ]