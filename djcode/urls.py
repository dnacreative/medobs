from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r"^$", direct_to_template, {"template": "index.html"}, "site_home"),
#	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#	(r'^admin/', include(admin.site.urls)),
)
