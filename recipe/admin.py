from django.contrib import admin
from recipe.models import Category, Container, Version, Ingredient, Step


class ContainerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Version)
admin.site.register(Ingredient)
admin.site.register(Step)
