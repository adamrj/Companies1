from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^companies/', include('companies.urls', namespace='companies')),
    url(r'^admin/', include(admin.site.urls)),
]
