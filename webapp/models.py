from django.db import models

class Candidato(models.Model):
	nome = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.nome

class Pagina(models.Model):
	candidato = models.ForeignKey(Candidato)
	titulo = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.titulo

