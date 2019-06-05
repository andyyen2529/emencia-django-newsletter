"""Urls for the emencia18 of emencia.django.newsletter"""
import os

from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
#from django.conf.urls import patterns
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.views.generic.base import RedirectView
from django.views.static import *
admin.autodiscover()

urlpatterns = [
                       url(r'^$', RedirectView.as_view(url='/admin/')),
                       url(r'^newsletters/', include('emencia.django.newsletter.urls')),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^admin/', include(admin.site.urls)),
                       ]
 
urlpatterns += [#'django.views.static',
                        url(r'^edn/(?P<path>.*)$', serve, #'serve'
                            {'document_root': os.path.join(os.path.dirname(__file__),
                                                           '..', 'emencia', 'django',
                                                           'newsletter', 'media', 'edn')}),]
