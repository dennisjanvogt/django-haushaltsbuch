# Generated by Django 3.2.7 on 2021-09-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rechnung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rechnung_datum', models.DateTimeField()),
                ('rechnung_betrag', models.FloatField(null=True)),
                ('rechnung_beschreibung', models.CharField(max_length=200)),
                ('rechung_kategorie', models.CharField(choices=[('Nahrung', 'Nahrung'), ('Technik', 'Technik'), ('Ausflüge', 'Ausflüge'), ('Sonstiges', 'Sonstiges')], max_length=20)),
            ],
        ),
    ]
