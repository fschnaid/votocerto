import os

def populate():
	add_cand('Aécio Neves')
	add_cand('Dilma Rousseff')


def add_cand(nome):
	c = Candidato.objects.get_or_create(nome=nome)[0]
	return c

if __name__ == '__main__':
    print "Criando candidatos..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'votosecreto.settings')
    import django
    django.setup()
    from webapp.models import Candidato, Pagina
    populate()
    print "Candidatos criados!"