from django.conf.urls import patterns, include, url
from django.contrib import admin
from test1.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get/coordinates', get_coordinates),
    url(r'^ivr', call_ivr),
    url(r'^$', home),
)
