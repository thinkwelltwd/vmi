
from django import forms
from .models import IndividualIdentifier

# Copyright Videntity Systems Inc.


class IndividualIdentifierForm(forms.ModelForm):

    class Meta:
        model = IndividualIdentifier
        fields = ['type', 'issuer', 'value', 'country', 'subdivision', 'uri']
