from django.contrib import admin
from django.urls import include, path, re_path
from .import views

urlpatterns = [

#estateapp/
    path('', views.IndexView.as_view(), name='index'),

#estateapp/1
    re_path(r'^(?P<pk>[0-9])/$', views.LocationView.as_view(), name='property'),

#estateapp/1/1
    re_path(r'^([0-9]+)/(?P<pk>[0-9])/$', views.PropertyDetail.as_view(), name='propertyview'),
]
