from django.conf.urls  import url
from backscratchers import views


urlpatterns = [
    url(r'^backscratchers/$', views.backscratcher_list),
    url(r'^backscratchers/(?P<pk>[0-9]+)/$', views.backscratcher_detail),
]
