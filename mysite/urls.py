from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import my.views

urlpatterns = [
	url(r'^$', my.views.index, name='index'),
	url(r'^my/', include('my.urls')),
    url(r'^admin/', admin.site.urls),
]
