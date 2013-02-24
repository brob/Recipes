from django.contrib import admin
from recipe.models import *


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Recipe, RecipeAdmin)
