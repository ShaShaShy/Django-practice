from django import forms
from myApp.models import Users

class userForm(forms.ModelForm):
	class Meta:
		model=Users
		fields='__all__'
			