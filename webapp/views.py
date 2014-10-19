from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from webapp.models import Candidato, Pagina
from webapp.forms import PaginaForm


def index(request):
	context = RequestContext(request)
	candidato_list = Candidato.objects.all()
	for candidato in candidato_list:
		candidato.url = encode_url(candidato.nome)

	context_dict = {'candidatos': candidato_list}



	return render_to_response('webapp/home.html', context_dict, context)

def candidato_funct(request, candidato_nome_url):
	context = RequestContext(request)
	candidato_nome = decode_url(candidato_nome_url)
	context_dict = {'candidato_nome': candidato_nome}
	context_dict['candidato_nome_url'] = candidato_nome_url

	candidato = Candidato.objects.get(nome=candidato_nome)
	paginas = Pagina.objects.filter(candidato=candidato)

	context_dict['paginas'] = paginas

	return render_to_response('webapp/candidato.html', context_dict, context)


def adicionar_pagina(request, candidato_nome_url):
	context = RequestContext(request)

	candidato_nome = decode_url(candidato_nome_url)

	if request.method == 'POST':
		form = PaginaForm(request.POST)

		if form.is_valid():
			pagina = form.save(commit=False)

			try:
				candidato = Candidato.objects.get(nome=candidato_nome)
				pagina.candidato = candidato
			except Candidato.DoesNotExist:
				return render_to_response('webapp/add_pagina.html', {}, context)

			pagina.views = 0

			pagina.save()

			return candidato_funct(request, candidato_nome_url)

		else:
			print form.errors
	else:
		form = PaginaForm()

	return render_to_response('webapp/add_pagina.html', {'candidato_nome_url': candidato_nome_url, 'candidato_nome':candidato_nome, 'form': form}, context)




	





############# DECODERS ####################

def decode_url(name):
	return name.replace('_', ' ')

def encode_url(name):
	return name.replace(' ', '_')

###########################################




# Create your views here.
