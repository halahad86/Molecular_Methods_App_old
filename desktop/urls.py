from django.conf.urls import patterns,include, url
from desktop import views
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/$', views.index, name='index'),
        url(r'^glossary/$', views.glossary, name='glossary'),
        url(r'^labs/$', views.labs, name='labs'),
        url(r'^admin/$', include(admin.site.urls)),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^videos/$', views.videos, name='videos'),
        url(r'^primersquizzes/$', views.primersquizzes, name='primersquizzes'),
        url(r'^project/$', views.project, name='project'),
        url(r'^pcrlab/$', views.pcrlab, name='pcrlab.html'),
        url(r'^revision/$', views.project, name='revision'),
)


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )