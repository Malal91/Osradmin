from django import forms
from django.contrib.auth.models import User
from .models import Membre, Categorie, Langage

class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=30, 
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Nom utilisateur',
                                   'class':'input-large span10',
                                   'required':'required'
                               }))
    password = forms.CharField(max_length=16,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Mot de passe',
                                   'class':'input-large span10',
                                   'required':'required'
                               }))
    
class MembreForm(forms.Form):
    username = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Nom utilisateur',
                                  'class': 'input-xlarge focused',
                                  'required': 'required'
                              }))
    first_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Prénom',
                                    'class': 'input-xlarge focused',
                                    'required': 'required'
                                }))
    last_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Nom',
                                    'class': 'input-xlarge focused',
                                    'required': 'required'
                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
                                    'placeholder': 'Email',
                                    'class': 'input-xlarge focused',
                                    'required': 'required'
                                }))
    site_web = forms.URLField(required=False,
                              widget=forms.TextInput(attrs={
                                    'placeholder': 'Site Web',
                                    'class': 'input-xlarge focused',
                                }))
    facebook = forms.URLField(required=False,
                              widget=forms.TextInput(attrs={
                                    'placeholder': 'Facebook',
                                    'class': 'input-xlarge focused'
                                }))
    twitter = forms.URLField(required=False,
                             widget=forms.TextInput(attrs={
                                    'placeholder': 'Twitter',
                                    'class': 'input-xlarge focused'
                                }))
    instagram = forms.URLField(required=False,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'Instagram',
                                    'class': 'input-xlarge focused'
                                }))
    linkedin = forms.URLField(required=False,
                              widget=forms.TextInput(attrs={
                                    'placeholder': 'Linkedin',
                                    'class': 'input-xlarge focused'
                                }))
    google_plus = forms.URLField(required=False,
                                 widget=forms.TextInput(attrs={
                                    'placeholder': 'Gougle+',
                                    'class': 'input-xlarge'
                                }))
    signature = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={
                                    'placeholder': 'Votre signature',
                                    'class': 'input-xlarge'
                                }))
    biographie = forms.CharField(required=False,
                                 widget=forms.Textarea(attrs={
                                    'placeholder': 'Un peu de biographie',
                                    'class': 'cleditor'
                                }))
        
    def clean(self):
        cleaned_data = super(MembreForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if username:
            if User.objects.filter(username=username):
                msg =u"Ce nom d'utilisateur existe déjà"
                self._errors["username"] = self.error_class([msg])
                del cleaned_data["username"]
            
            if User.objects.filter(email=email):
                msg=u"Cet email à déjà été utiliser"
                self._errors["email"] = self.error_class([msg])
                del cleaned_data["email"]
        return cleaned_data
    
class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('categorie',)
        widget = {
            'categorie': forms.fields.TextInput(attrs={
                'placeholder': 'Ajouter la categorie du langage ou de la matière',
                'class': 'input-xlarge',
                'required': 'true'
            })
        }
        
    def clean(self):
        cleaned_data = super(CategorieForm, self).clean()
        categorie = cleaned_data.get('categorie')
        if categorie:
            if Categorie.objects.filter(categorie=categorie):
                msg=u"Cette categorie existe déjà"
                self._errors['categorie'] = self.error_class([msg])
                del cleaned_data['categorie']
        return cleaned_data

class LangageForm(forms.ModelForm):
    class Meta:
        model = Langage
        fields = ('langage','categorie',)
        widget = {
            'langage': forms.fields.TextInput(attrs={
                'placeholder': 'Saisir le langage ou la matière',
                'class': 'input-xlarge'
            })
        }
        
    def clean(self):
        cleaned_data = super(LangageForm, self).clean()
        langage = cleaned_data.get('langage')
        if langage:
            if Langage.objects.filter(langage=langage):
                msg=u"Ce langage ou matière existe déjà"
                self._errors['langage'] = self.error_class([msg])
                del cleaned_data['langage']
        return cleaned_data