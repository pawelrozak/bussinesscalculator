from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
from bc_calculation import urls as bc_calculation_urls

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('calculation/', include('bc_calculation.urls')),
    path('admin/', admin.site.urls),
]
