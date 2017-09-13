from django.conf.urls import url
from django.urls import reverse

from chat import views

urlpatterns = [
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<chat_room_id>[0-9]+)/$', views.chat_room, name='chat_room'),

              ]
