# Generated by Django 3.2.7 on 2021-09-18 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ausgaben', '0002_alter_rechnung_rechnung_datum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rechnung',
            old_name='rechung_kategorie',
            new_name='rechnung_kategorie',
        ),
    ]