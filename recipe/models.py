from django.db import models
#from tagging.fields import TagField
from django.contrib import admin
#import django.forms as forms
from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
import jsonfield


 
class Recipe(models.Model):
    title = models.TextField(max_length=200)
    summary = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    ingredients = jsonfield.JSONField()
    steps = jsonfield.JSONField()

    class Meta:
        ordering = ['title']


    def __unicode__(self):
        return self.title
