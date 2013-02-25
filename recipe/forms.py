from django.db import models
#from tagging.fields import TagField
from django.contrib import admin
import django.forms as forms
from django.forms.formsets import formset_factory
from django.forms import ModelForm
from django import forms
#from django.forms.models import inlineformset_factory
import jsonfield
from recipe.models import *


class IngredientForm(forms.Form):
	amt = forms.CharField()
	ingredient = forms.CharField()

class StepForm(forms.Form):
	step = forms.CharField()

class VersionForms(forms.Form):
	class Meta:
		model = Recipe