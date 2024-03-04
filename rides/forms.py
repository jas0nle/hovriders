from django import forms
from .models import Person


class RideForm(forms.Form):
  stateSearch = forms.CharField(label='Search Destination State', max_length=64, required=False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []