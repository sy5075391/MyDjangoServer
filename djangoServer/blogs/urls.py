from django.conf.urls import url
from . import views

from django.conf.urls import url, include


urlpatterns = [
    url(r'^post/\d+/$', views.post_detial, name='post_detial'),
    url(r'^post/$', views.post_list, name='post_list'),
]

# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
#     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detial, name='post_detail'),
# ]