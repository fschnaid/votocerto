from django.conf.urls import patterns, url
from webapp import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^candidato/(?P<candidato_nome_url>\w+)/$', views.candidato_funct, name='candidato'),
	url(r'^candidato/(?P<candidato_nome_url>\w+)/adicionar_pagina/$', views.adicionar_pagina, name='adicionar_pagina'),
	)

