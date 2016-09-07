from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testLocalHost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/$', 'testLocalHost.a.hello',name='hello'),
	url(r'^current_time/$', 'testLocalHost.a.current_time',name='current_time'),

    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATICFILES_DIRS, 'show_indexes': True}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',),
    url(r'^test_html/$', 'testLocalHost.a.test_html',name='test_html'),
    url(r'^user_info/$', 'testLocalHost.a.user_info',name='user_info'),
 	url(r'^user_info1/$', 'testLocalHost.a.user_info1',name='user_info1'),
    url(r'^product_info/$', 'testLocalHost.a.product_info',name='product_info'),


    #url(r'^search/$', 'testLocalHost.a.search',name='search'),

    url(r'^search/', include('haystack.urls')),  

)
