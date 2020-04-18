from django.forms import ModelForm
from myapp.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model=Place
        fields=("city",)
