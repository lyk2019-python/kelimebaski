from django import forms


class YorumFormu(forms.Form):
    icerik = forms.CharField(widget=forms.Textarea(attrs={"cols":20, "rows":3}), max_length=280, min_length=3)
