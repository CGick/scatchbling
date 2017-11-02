from django.conf.urls  import url
from rest_framework.urlpatterns import format_suffix_patterns
from backscratchers import views


urlpatterns = [
    url(r'^backscratchers/$', views.BackscratcherList.as_view()),
    url(r'^backscratchers/(?P<pk>[0-9]+)/$', views.BackscratcherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
