from django.shortcuts import render, redirect

from .models import Rechnung
from .forms import RechnungForm
from .filters import RechnungFilter

import datetime


# Create your views here.
def index(request):

    rechnungen = Rechnung.objects.all().order_by('-datum')
    today = datetime.date.today()
    aktueller_monat = datetime.datetime.now().strftime("%B").upper()
    aktuelle_rechnungen = []
    aktuelle_rechnungen = rechnungen.filter(datum__year=today.year, datum__month=today.month)
    
    
    # aktuelle Summe ermitteln
    summe_monat = 0.0
    if len(aktuelle_rechnungen) > 0:
        for rechnung in aktuelle_rechnungen:
            summe_monat += rechnung.betrag


    # letzte Summe ermitteln
    prev = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    letzte_rechnungen = rechnungen.filter(datum__year=prev.year, datum__month=prev.month)

    summe_letzter_monat = 0.0
    for rechnung in letzte_rechnungen:
        summe_letzter_monat += rechnung.betrag


    # top Kategorie ermitteln
    KATEGORIEN = ("Lebensmittel", "Technik", "Ausflüge", "Sonstiges")
    kategorie_summe_max = 0.0
    top_kategorie = "Keine"
    for kategorie in KATEGORIEN:
        kategorie_summe = sum([rechnung.betrag for rechnung in aktuelle_rechnungen if rechnung.kategorie == kategorie])
        if kategorie_summe > kategorie_summe_max:
            top_kategorie = kategorie
            kategorie_summe_max = kategorie_summe


    context = {
        "rechnungen": aktuelle_rechnungen,
        "summe_monat": summe_monat,
        "top_kategorie": top_kategorie,
        "summe_letzter_monat": summe_letzter_monat,
        "aktueller_monat": aktueller_monat,
        }

    return render(request, 'ausgaben/index.html', context)



def rechnung_form(request):
    rechnungForm = RechnungForm()
    if request.method == 'POST':
        rechnungForm = RechnungForm(request.POST)
        if rechnungForm.is_valid():
            rechnungForm.save()
            return redirect("index_ausgaben")
    else:
        rechnungForm = RechnungForm()

    context = {
        "form": rechnungForm,
        }

    return render(request, 'ausgaben/rechnung_form.html', context)



def update_rechnung(request, id):

    rechnung = Rechnung.objects.get(id=id)
    updateForm = RechnungForm(instance=rechnung)

    if request.method == 'POST':
        updateForm = RechnungForm(request.POST, instance=rechnung)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('index_ausgaben')

    context = {'form':updateForm,}
    
    return render(request, 'ausgaben/rechnung_form.html', context)



def delete_rechnung(request, id):
	rechnung = Rechnung.objects.get(id=id)
	if request.method == "POST":
		rechnung.delete()
		return redirect('index_ausgaben')

	context = {'rechnung':rechnung}

	return render(request, 'ausgaben/rechnung_loeschen.html', context)


def analyse(request):

	rechnungen = Rechnung.objects.all().order_by('-datum')

	myFilter = RechnungFilter(request.GET, queryset=rechnungen)
	rechnungen = myFilter.qs 

	context = {
        'rechnungen': rechnungen,
	    'myFilter': myFilter,
    }

	return render(request, 'ausgaben/analyse.html',context)
