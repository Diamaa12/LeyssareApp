from .models import LeyssareMembres
from django import forms


class MyForm(forms.Form):
    username = forms.CharField(max_length=10, required=True, strip=True)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)

    def clean_username(self):
        psd = self.cleaned_data.get('username')
        if len(psd)>10:
            raise forms.ValidationError('Le pseudo ne doit pas contenir plus de 10 caractéres.')
        return psd
    def clean_password(self):
        psw = self.cleaned_data.get('password1')
        if len(psw)<8:
            raise forms.ValidationError('Le mot de passe doit contenir au moins 8 caractères.')
        return psw
#Classe qui gére le foumulaire de nos membres
class FormUserMembres(forms.ModelForm):
    class Meta:
        model = LeyssareMembres
        fields = [
            'nom',
            'prenom',
            'pays',

        ]
        labels = {
            'name':'Votre nom',
            'prenom':'Votre prénom',
            'contry':'Votre pays de résidence',

        }
class Authentification(forms.Form):
    id_number = forms.CharField(label='VOTRE CODE PERSONNEL ICI')



class MyUserForm(forms.Form):
    user_name = forms.CharField(label='Your username')
    pass_word = forms.CharField(label='Your password', widget=forms.PasswordInput())