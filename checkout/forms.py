from typing import Any
from django import forms
from checkout.models import CheckoutLine


class CheckOutLineForm(forms.ModelForm):
    class Meta:
        model = CheckoutLine
        exclude = ('checkout', 'product',)

   
    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product') 
        super(CheckOutLineForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(CheckOutLineForm,self).clean()
        quantity = self.cleaned_data.get('quantity')
        product_stock = self.product.stock
        if quantity > product_stock:
            self.add_error('quantity','insufficient stock')
        
        return self.cleaned_data

    