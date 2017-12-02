from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$',views.registerUser, name='register'),
    url(r'^my-time/$',views.AvailabilityListView.as_view(), name='my-time'),
    url(r'^add-time/$',views.getAvailableTime, name='add-time'),
    url(r'^groups/$', views.GroupListView.as_view(), name='group-list'),
    url(r'^add-group/$', views.addGroupView, name='add-group'),
]