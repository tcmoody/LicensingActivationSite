from django import forms
from models import merchant
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
import views

class create_user_form(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class create_merchant_form(ModelForm):
	class Meta:
		model = merchant
		fields = ('merchantName',)

def merchant_choices():
	choices = views.merchantNameList
	return choices

class select_merchant_form(forms.Form):
	def __init__(self, *args, **kwargs):
		super(select_merchant_form, self).__init__(*args, **kwargs)
		self.fields['merchant_choice_field'] = forms.ChoiceField(choices=merchant_choices())