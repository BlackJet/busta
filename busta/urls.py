from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.post_view.home', name='home'),
    url(r'^get_post/$', 'core.post_view.get_post', name='get'),
    url(r'^add_post/$', 'core.post_view.add_post', name='add'),
    url(r'^u/(?P<login>[a-z0-9_]{1,30})/(?P<name>[a-z0-9_]{1,30})/$', 'core.post_view.open_post', name='open'),
    # url(r'^busta/', include('busta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
