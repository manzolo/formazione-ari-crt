from django.shortcuts import render, get_object_or_404
from .models import Lezione

def lista_lezioni(request):
    lezioni = Lezione.objects.all().order_by('numero')
    context = {'lezioni': lezioni}
    return render(request, 'lezioni/lista_lezioni.html', context)

def dettaglio_lezione(request, lezione_id):
    lezione = get_object_or_404(Lezione, pk=lezione_id)
    return render(request, 'lezioni/dettaglio_lezione.html', {'lezione': lezione})
