from django import forms
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, URLInput, PasswordInput, HiddenInput, DateInput, DateTimeInput, TimeInput, Textarea, CheckboxInput, Select, SelectMultiple, RadioSelect
from .models import *






class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        # fields = '__all__'
        fields = ['id',
                  'prenom',
                  'nom',
                  'naissance',
                  'sexe',
                  'adresse',
                  'telephone',
                  'email',
                  'lieu_de_travail',
                  'id_number',
                  'id_plaque',
                  'gilet_couleur',
                  'conjoint',
                  'pere_cin_nif',
                  'mere_cin_nif',

                  'date_created',
                  'created_by',
                  'date_modified',
                  'modified_by'
                  ]
        widgets = {
                    'id': HiddenInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'reference',}),


                    'prenom':TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Prénom',},
                                #error_messages={'unique': u'My custom message'}
                                ),

                    'nom':TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Nom de famille',},
                                #error_messages={'unique': u'My custom message'}
                                ),

                    'naissance': DateInput(format=('%Y-%m-%d'),
                                attrs={'class': 'form-control',
                                'placeholder': 'Date de naissance',
                                'type': 'date'}),
                    'sexe': Select(attrs={
                                'class': 'form-control',
                                'placeholder': 'Sexe',}),
                    'adresse':TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Adresse',},
                                #error_messages={'unique': u'My custom message'}
                                ),
                    'telephone': TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Prénom',
                                'type':'tel',
                                'pattern':'[0-9]{3}-[0-9]{4}-[0-9]{4}',
                                'title': "Doit respecter ce format d'exemple: 509-0000-0000",
                                },

                                #error_messages={'unique': u'My custom message'}
                                ),
                    'email': TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Email',
                                'type':'email',
                                'title': "Doit respecter ce format d'exemple: xxx@site.com",
                                },
                                #error_messages={'unique': u'My custom message'}
                                ),
                    'lieu_de_travail': Select(attrs={
                                'class': 'form-control',
                                'placeholder': 'Station/Lieu de travail',}),
                    'id_number':TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Numéro d'indentification unique",
                                'pattern':'[0-9]{10}',
                                'title': "Doit contenir uniquement 10 chiffres",
                                },
                                #error_messages={'unique': u'My custom message'}
                                ),
                    'id_plaque':TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Numéro de plaque(Moto)",
                                'pattern':'[A-Za-z]{2}-[0-9]{5}',
                                'title': "Doit respecter ce format d'exemple:BB-00000",
                                },),
                    'gilet_couleur':Select(attrs={
                                'class': 'form-control',
                                'placeholder': 'Couleur de gilet',}),
                    'conjoint': TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Numéro d'indentification unique du/de la conjoint(e)",
                                'pattern':'[0-9]{10}',
                                'title': "Doit contenir uniquement 10 chiffres",
                                },),
                    'pere_cin_nif':TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Numéro d'indentification unique du père",
                                'pattern':'[0-9]{10}',
                                'title': "Doit contenir uniquement 10 chiffres",
                                },),
                    'mere_cin_nif': TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Numéro d'indentification unique de la mère",
                                'pattern':'[0-9]{10}',
                                'title': "Doit contenir uniquement 10 chiffres",
                                },),


                    'date_created':  HiddenInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'date_created',}),
                    'created_by':  HiddenInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'created_by',}),
                    'date_modified':  HiddenInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'date_modified',}),
                    'modified_by': HiddenInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'modified_by',}),

        }
    def __init__(self, *args, **kwargs):
        super(PersonneForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields['prenom'].label = "Prénom"
            self.fields['naissance'].label = "Date de naissance"
            self.fields['telephone'].label = "Téléphone (509-XXXX-XXXX)"
            self.fields['lieu_de_travail'].label = "Station/Lieu de travail"
            self.fields['id_number'].label = "NIU (10 chiffres)"
            self.fields['id_plaque'].label = "Numéro de plaque(Moto)"
            self.fields['gilet_couleur'].label = "Couleur de gilet"
            self.fields['conjoint'].label = "NIU du/de la conjoint(e) (10 chiffres)"
            self.fields['pere_cin_nif'].label = "NIU du père (10 chiffres)"
            self.fields['mere_cin_nif'].label = "NIU de la mère (10 chiffres)"



            #Chmps non-obligatoires
            self.fields['email'].required = False
            self.fields['lieu_de_travail'].required = False
            self.fields['id_plaque'].required = False
            self.fields['gilet_couleur'].required = False
            self.fields['conjoint'].required = False
            self.fields['pere_cin_nif'].required = False
            self.fields['mere_cin_nif'].required = False

            self.fields['date_created'].required = False
            self.fields['created_by'].required = False
            self.fields['date_modified'].required = False
            self.fields['modified_by'].required = False
