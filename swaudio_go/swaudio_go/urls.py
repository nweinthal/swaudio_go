from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'requests.views.res_request', name='home'),
    url(r'^logout/', 'backend.views.logout_view', name='logout'),
    url(r'^request/', 'requests.views.res_request', name='reservation request'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
