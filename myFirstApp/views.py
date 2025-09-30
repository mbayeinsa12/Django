from django.http import HttpResponse
from django.template import loader
from .models import Etudiant

def apprenants(request):
  etudiants = Etudiant.objects.all().values()
  template = loader.get_template('all_etudiants.html')
  context = {
    'etudiants': etudiants,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  etudiant = Etudiant.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'etudiant': etudiant,
  }
  return HttpResponse(template.render(context, request))