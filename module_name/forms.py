from django import forms
from module_name.models import Module_name

class Module_nameForm(forms.ModelForm):

    class Meta:
        model=Module_name
        fields="__all__"