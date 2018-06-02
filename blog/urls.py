from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<slug>[\w-]+)/edit/$', views.post_edit, name='post_edit'),
]
