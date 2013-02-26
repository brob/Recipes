from django.db import models
#from tagging.fields import TagField
from django.contrib import admin
import django.forms as forms
from django.forms import ModelForm
from django import forms
from django.forms.formsets import formset_factory
import jsonfield
from django.forms.widgets import *
from django.template.defaultfilters import slugify

 
class Recipe(models.Model):
    title = models.TextField(max_length=200)
    summary = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
#    ingredients = jsonfield.JSONField()
#    steps = jsonfield.JSONField()

    class Meta:
        ordering = ['title']


    def __unicode__(self):
        return self.title

class Version(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredients = jsonfield.JSONField()
	steps = jsonfield.JSONField()
	Note = models.TextField(blank=True)




# Forms
class IngredientForm(forms.Form):
	amt = forms.CharField()
	ingredient = forms.CharField()

class StepForm(forms.Form):
	step = forms.CharField()

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		widgets = {
			'slug': forms.HiddenInput(),
		}
	def save(self, *args, **kwargs):
		self.fields['slug'] = slugify(self.fields['title'])
		super(RecipeForm, self).save(*args, **kwargs)

class VersionForm(forms.ModelForm):
	class Meta:
		model = Version
		widgets = {
			'recipe' : forms.HiddenInput(),
			'ingredients' : forms.HiddenInput(),
			'steps' : forms.HiddenInput(),
		}
		