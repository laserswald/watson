from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^homework/$', views.HomeworkIndex.as_view(), name='homework_index'),
    url(r'^schedule/$', views.ScheduleIndex.as_view(), name='schedule_index'),
    url(r'^wishlist/$', views.WishlistIndex.as_view(), name='wishlist_index'),
    url(r'^messages/$', views.MessagesIndex.as_view(), name='messages_index')
]
