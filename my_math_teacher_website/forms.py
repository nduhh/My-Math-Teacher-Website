from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your Message',
            'rows': 5,
        }),
    )

class WaitingListForm(forms.Form):
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    school = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'School (optional)'})
    )
    grade = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Grade (optional)'})
    )
    province = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Province (optional)'})
    )    