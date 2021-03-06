# Generated by Django 3.2.7 on 2021-09-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausgaben', '0003_rename_rechung_kategorie_rechnung_rechnung_kategorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rechnung',
            old_name='rechnung_beschreibung',
            new_name='beschreibung',
        ),
        migrations.RenameField(
            model_name='rechnung',
            old_name='rechnung_betrag',
            new_name='betrag',
        ),
        migrations.RenameField(
            model_name='rechnung',
            old_name='rechnung_datum',
            new_name='datum',
        ),
        migrations.RemoveField(
            model_name='rechnung',
            name='rechnung_kategorie',
        ),
        migrations.AddField(
            model_name='rechnung',
            name='kategorie',
            field=models.CharField(choices=[('Lebensmittel', 'Lebensmittel'), ('Technik', 'Technik'), ('Ausflüge', 'Ausflüge'), ('Sonstiges', 'Sonstiges')], default='asd', max_length=20),
            preserve_default=False,
        ),
    ]
