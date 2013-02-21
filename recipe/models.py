from django.db import models
#from tagging.fields import TagField
from django.contrib import admin
#import django.forms as forms
from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory


        


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120)
   # parent = models.ForeignKey('self', null=True, blank=True, related_name='child_set')
    #order_index = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
    #    ordering = ["order_index"]



 
class Container(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
  # prep_time = models.CharField(max_length=100, blank=True) # This field type is a guess.
  # sources = models.ManyToManyField(Source, blank=True)
  # category = models.ForeignKey(Category, blank=True, null=True)


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

class ContainerForm(ModelForm):
    class Meta:
        model = Container

class Version(models.Model):
	Container = models.ForeignKey(Container)
	#Ingredient = models.ManyToManyField('Ingredient', blank=True)
	#Step = models.ManyToManyField('Step', blank=True)
	Note = models.TextField(blank=True)

class VersionForm(ModelForm):
    class Meta:
        model = Version
        
        widgets = {
            'Container': forms.HiddenInput()
          }
	
class Ingredient(models.Model):
	Ingredient = models.CharField(max_length=500)
	Recipe = models.ForeignKey(Version, blank=True)
	def __unicode__(self):
		return self.Ingredient	
		
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient		

class Step(models.Model):
	Step = models.TextField()
	Order = models.IntegerField(blank=True)
	Recipe = models.ForeignKey(Version, blank=True)
	
	def __unicode__(self):
		return self.Step


class StepForm(ModelForm):
    class Meta:
        model = Step


IngredientFormSet = inlineformset_factory(Version, 
    Ingredient, 
    can_delete=False)
    
StepFormSet = inlineformset_factory(Version, 
    Step, 
    can_delete=False)