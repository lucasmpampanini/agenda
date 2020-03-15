from django.shortcuts import render
from core.models import Eevnto
# Create your views here.

def lista_eventos(request):
    evento = Eevnto.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)