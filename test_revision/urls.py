from django.conf.urls import patterns, include, url

from django.contrib import admin
from test_app.views import articleDV,articleUV
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_revision.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/(?P<pk>[\d]+)/$', articleUV.as_view()),
    url(r'^delete/(?P<pk>[\d]+)/$', articleDV.as_view()),
)
