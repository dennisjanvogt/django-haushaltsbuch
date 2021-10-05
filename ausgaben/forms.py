from django import forms
from crispy_forms.helper import FormHelper

from .models import Rechnung


class RechnungForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Rechnung
        fields = "__all__"

    
