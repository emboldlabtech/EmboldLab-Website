from django import forms
from django.contrib import admin
from django.utils.text import slugify
from .models import Bootcamp,Category,Registration,Blogpost,Cohort3Registration
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User

class BootcampForm(forms.ModelForm):
    class Meta:
        model = Bootcamp
        exclude = ('slug', 'thumbnail', 'parent')


class Cohort3RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')


    class Meta:
        model = Cohort3Registration
        fields = [
            'name', 'email', 'phone', 'laptop', 'program', 'course',
            'level', 'source', 'location', 'pledge_dedication', 'refer_code', 'course_price','password1', 'password2'
        ]
        widgets = {
            'course_price': forms.HiddenInput(),
        }
        labels = {
            'name': 'Surname and First Name',
            'email': 'Email',
            'phone': 'WhatsApp Phone Number',
            'laptop': 'Do you have access to a laptop?',
            'program': 'What are you applying for?',
            'course': 'Select Course',
            'level': 'What do you see yourself as?',
            'source': 'How did you hear about us?',
            'location': 'Location',
            'pledge_dedication': 'I pledge to make the most of this opportunity by dedicating myself wholeheartedly to my studies, attendance of all classes sessions and projects.',
            'refer': 'Referral Code',
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug', 'ordering', 'parent')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']


class CohortUpdateForm(forms.ModelForm):
    class Meta:
        model = Cohort3Registration
        fields = [
            'profile_picture', 'phone', 'name',
            'week_1', 'week_2', 'week_3', 'week_4',
            'week_5', 'week_6', 'week_7', 'week_8',
            'certificate','scheduled_classes', 'calendar'
        ]

    def __init__(self, *args, **kwargs):
        super(CohortUpdateForm, self).__init__(*args, **kwargs)
        # Set required=False for optional fields
        optional_fields = [
            'week_1', 'week_2', 'week_3', 'week_4',
            'week_5', 'week_6', 'week_7', 'week_8',
            'certificate','scheduled_classes', 'calendar'
        ]
        for field in optional_fields:
            self.fields[field].required = False

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



from django import forms
from django.contrib.auth.models import User
from .models import Message
class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.filter(username__in=['Instructor', 'Support']),
        label="To"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Type your message here...'}),
        label="Message"
    )

    class Meta:
        model = Message
        fields = ['recipient', 'message']