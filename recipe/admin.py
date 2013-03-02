from django.contrib import admin
from recipe.models import *


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('created_by',)
    
    def save_form(self,request, form, change):
		obj = super(RecipeAdmin, self).save_form(request, form, change)
		
		if not change:
			obj.created_by = request.user
    		return obj    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Version)
