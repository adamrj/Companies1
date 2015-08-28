from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'companies.views.index', name='index'),
    url(r'^new$', 'companies.views.new', name='new'),
    url(r'^create$', 'companies.views.create', name='create'),
    url(r'^(?P<company_id>[0-9]+)$', 'companies.views.info', name='info'),
    url(r'^(?P<company_id>[0-9]+)/edit_view$', 'companies.views.edit_view', name='edit_view'),
    url(r'^(?P<company_id>[0-9]+)/edit$', 'companies.views.edit', name='edit'),
    url(r'^(?P<company_id>[0-9]+)/delete$', 'companies.views.delete', name='delete'),

]
