from django import forms

from userprofile.models  import Adresses, UserProfile


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = Adresses
        fields ='__all__'





class VisitorShippingAddressForm(ShippingAddressForm):
    email = forms.EmailField()
 

 

class EditShippingAddressForm(forms.Form):
    """Form definition for EditShippingAddress."""
    address =  forms.ModelChoiceField(queryset=Adresses.objects.none())
   
   
    def __init__(self, *args, **kwargs):
       self.user = kwargs.pop('user')
       super(EditShippingAddressForm, self).__init__(*args, **kwargs)
       self.fields['address'].queryset = UserProfile.objects.get(user=self.user).user_adress.all()

   