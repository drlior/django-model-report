# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from model_report import report
report.autodiscover()


urlpatterns = (url(r'^admin/', include(admin.site.urls)),
    url(r'', include('model_report.urls')),
)
