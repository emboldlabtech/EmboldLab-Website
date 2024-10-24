from django import forms
from django.contrib import admin
from django.utils.text import slugify
from .models import Bootcamp,Category,Registration,Blogpost,BootcampRegistration
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BootcampForm(forms.ModelForm):
    class Meta:
        model = Bootcamp
        exclude = ('slug', 'thumbnail', 'parent')


class BootcampRegistrationForm(forms.ModelForm):
    class Meta:
        model = BootcampRegistration
        fields = [
            'name', 'email', 'phone', 'laptop_access', 'program', 'course',
            'level', 'source', 'location', 'proof_of_payment', 'referral_code'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug', 'ordering', 'parent')

class RegistrationForm(forms.ModelForm):
    bootcamp_price = forms.DecimalField(widget=forms.HiddenInput())  # Add this line

    class Meta:
        model = Registration
        fields = [
            'first_name', 'middle_name', 'surname', 'email',
            'gender', 'bootcamp', 'level', 'laptop_access',
            'full_duration_commitment', 'source', 'pledge_dedication',
            'pledge_terms','phone', 'bootcamp_price','referral_code'
        ]
        widgets = {
            'bootcamp': forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'referral_code': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'laptop_access': forms.Select(attrs={'class': 'form-select'}),
            'full_duration_commitment':forms.Select(attrs={'class': 'form-select'}),
            'source': forms.Select(attrs={'class': 'form-select','label':''}),
            'pledge_dedication': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pledge_terms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bootcamp_price': forms.HiddenInput(),
        }
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        pledge_dedication = cleaned_data.get('pledge_dedication')
        pledge_terms = cleaned_data.get('pledge_terms')

        if not pledge_dedication:
            self.add_error('pledge_dedication', 'You must pledge your dedication.')

        if not pledge_terms:
            self.add_error('pledge_terms', 'You must accept the terms.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

    def __init__(self, *args, **kwargs):
        bootcamp_price = kwargs.pop('bootcamp_price', None)
        super().__init__(*args, **kwargs)
        if bootcamp_price is not None:
            self.fields['bootcamp_price'].initial = bootcamp_price



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        exclude = ('slug', 'thumbnail')
