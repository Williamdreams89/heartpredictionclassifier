from django import forms
from .models import DiagosticFeatures



class HeartDiagnosesForm(forms.ModelForm):
    class Meta:
        model = DiagosticFeatures
        fields = "__all__"

    