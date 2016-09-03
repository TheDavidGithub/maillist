from django.conf.urls import patterns, url
from maillist.views import test, synchro

urlpatterns = patterns(
    '',
    url(r'^$', test),
    url(r'^synchro/$', synchro),
)
