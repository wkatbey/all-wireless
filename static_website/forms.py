from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.CharField(label='Email')
    inquiry = forms.CharField(
        label = 'Let us know what you need!',
        widget = forms.Textarea(
            attrs = {'rows': 10, 'cols': 50}
        )
    )
