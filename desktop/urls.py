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
        url(r'^checkans/$', views.checkans, name='checkans'),
        url(r'^generalquizzes/$', views.generalquizzes, name='generalquizzes'),
        url(r'^restrictionquizzes/$', views.restrictionquizzes, name='restrictionquizzes'),
        url(r'^dataquizzes/$', views.dataquizzes, name='dataquizzes'),
        url(r'^project/$', views.project, name='project'),
        url(r'^pcrlab/$', views.pcrlab, name='pcrlab'),
        url(r'^ligation/$', views.ligation, name='ligation'),
        url(r'^bwscreening/$', views.bwscreening, name='bwscreening'),
        url(r'^plasmid/$', views.plasmid, name='plasmid'),
        url(r'^dna/$', views.dna, name='dna'),
        url(r'^quantpcr/$', views.quantpcr, name='quantpcr'),
        url(r'^revision/$', views.revision, name='revision'),
        url(r'^converterconcentration/$', views.converterconcentration, name='converterconcentration'),
        url(r'^converterdilutions/$', views.converterdilutions, name='converterdilutions'),
        url(r'^convertermass/$', views.convertermass, name='convertermass'),
        url(r'^convertermolarity/$', views.convertermolarity, name='convertermolarity'),
        url(r'^convertervolume/$', views.convertervolume, name='convertervolume'),
        url(r'^mapping/(?P<question_num>\w+)/$', views.mapping, name='mapping'),
        url(r'^pcrlabpdf/$', views.pcrlabpdf, name='pcrlabpdf'),
        url(r'^ligationlabpdf/$', views.ligationlabpdf, name='ligationlabpdf'),
        url(r'^bwslabpdf/$', views.bwslabpdf, name='bwslabpdf'),
        url(r'^plasmidlabpdf/$', views.plasmidlabpdf, name='plasmidlabpdf'),
        url(r'^dnalabpdf/$', views.dnalabpdf, name='dnalabpdf'),
        url(r'^qpcrlabpdf/$', views.qpcrlabpdf, name='qpcrlabpdf'),
        url(r'^Electrophoresis/$', views.Electrophoresis, name='Electrophoresis'),
        url(r'^Sequence_Analysis/$', views.Sequence_Analysis, name='Sequence_Analysis'),
        url(r'^Ligation_Calculations/$', views.Ligation_Calculations, name='Ligation_Calculations'),
        url(r'^QPCR_Exercises/$', views.QPCR_Exercises, name='QPCR_Exercises'),
        url(r'^Primer_Design_Exercise/$', views.Primer_Design_Exercise, name='Primer_Design_Exercise'),
        url(r'^Restriction_Mapping_Exercise/$',views.Restriction_Mapping_Exercise, name='Restriction_Mapping_Exercise'),
)


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )