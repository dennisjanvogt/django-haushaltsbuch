import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter

from .models import Rechnung

class RechnungFilter(django_filters.FilterSet):

	KATEGORIEN = (
        ("Lebensmittel", "Lebensmittel"),
        ("Technik", "Technik"),
        ("Ausflüge", "Ausflüge"),
        ("Sonstiges", "Sonstiges")
    )

	start_date = DateFilter(field_name="datum", lookup_expr='gte', label="Start")
	end_date = DateFilter(field_name="datum", lookup_expr='lte', label="Ende")
	beschreibung = CharFilter(field_name="beschreibung", label="Beschreibung")
	kategorie = ChoiceFilter(field_name="kategorie", label="Kategorie", choices=KATEGORIEN)
	#note = CharFilter(field_name='note', lookup_expr='icontains')

	class Meta:
		model = Rechnung
		fields = '__all__'
