from django import forms

PRODUCT_QTY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddItemForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QTY_CHOICES, coerce=int)
    update_qty = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
