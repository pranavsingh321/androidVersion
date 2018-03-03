from django.conf.urls import url, include
from uploadapi import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^applications$', cache_page(60)(views.CreateViewApplications.as_view()), name='application_list'),
    url(r'^applications/(?P<pk>[0-9]+)$', views.DetailsViewApplication.as_view(), name='application_detail'),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)
