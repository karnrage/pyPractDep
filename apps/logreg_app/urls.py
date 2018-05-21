
# urlpatterns = [ 
#    url(r'^$', index, name = 'my_index'), 
# ]

from django.conf.urls import url, include
from django.contrib import admin
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = "create"), #in views need to have a route with the same name
    url(r'^success$', views.success, name = 'success'), # routing, now routing to success definition. make a new success def on views page
    url(r'^login$', views.login, name = 'login'),
    url(r'^logout$', views.logout, name = 'logout')


    # url(r'^user/(?P<user_id>\d+)/update$', views.update, name = 'update'),
    # url(r'^user/(?P<user_id>\d+)/delete$', views.delete, name = 'delete')
]