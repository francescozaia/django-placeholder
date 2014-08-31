from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'placeholder.views.index', name='homepage'),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', 'placeholder.views.placeholder', name='placeholder'),

)

