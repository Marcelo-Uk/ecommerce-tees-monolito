from django import forms
from .models import Cartao
import re

class CartaoAdminForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = "__all__"

    def clean_numero_cartao(self):
        num = (self.cleaned_data.get("numero_cartao") or "").replace(" ", "")
        if not num.isdigit() or len(num) != 16:
            raise forms.ValidationError("Informe exatamente 16 dígitos numéricos.")
        return num

    def clean_cvv(self):
        cvv = self.cleaned_data.get("cvv") or ""
        if not cvv.isdigit() or len(cvv) != 3:
            raise forms.ValidationError("CVV deve ter 3 dígitos numéricos.")
        return cvv

    def clean_data_validade(self):
        val = self.cleaned_data.get("data_validade") or ""
        if not re.match(r"^\d{2}/\d{2}$", val):
            raise forms.ValidationError("Use o formato MM/AA.")
        mm, aa = val.split("/")
        if not (1 <= int(mm) <= 12):
            raise forms.ValidationError("Mês inválido (1–12).")
        return val
