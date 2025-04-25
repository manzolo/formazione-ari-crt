from django.shortcuts import render, get_object_or_404
from .models import Lezione

def lista_lezioni(request):
    lezioni_ordinate = Lezione.objects.all().order_by('numero')
    return render(request, 'lezioni/lista_lezioni.html', {'lezioni': lezioni_ordinate})

def dettaglio_lezione(request, lezione_id):
    lezione = get_object_or_404(Lezione, pk=lezione_id)
    return render(request, 'lezioni/dettaglio_lezione.html', {'lezione': lezione})
