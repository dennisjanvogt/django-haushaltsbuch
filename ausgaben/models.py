from django.db import models

# Create your models here.
class Rechnung(models.Model):

    KATEGORIEN = (
        ("Lebensmittel", "Lebensmittel"),
        ("Technik", "Technik"),
        ("Ausflüge", "Ausflüge"),
        ("Sonstiges", "Sonstiges")
    )

    datum = models.DateField()
    betrag = models.FloatField(null=True)
    beschreibung = models.CharField(max_length=200)
    kategorie = models.CharField(max_length=20, choices=KATEGORIEN)

    

    def __str__(self):
        return f"{self.datum}: {self.beschreibung}"