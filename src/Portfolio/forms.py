from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'id':'name','placeholder':'Name', 'type':'text'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'id':'email','placeholder':'Email', 'type':'email'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'id':'subject','placeholder':'Subject', 'type':'text'}))
	message = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'id':'messagee','placeholder':'Message', 'type':'text'}))

	class Meta:
		model = Contact
		fields = [ "name","email","subject","message" ]