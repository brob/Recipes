# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from recipe.models import *
from recipe.forms import *
from django.forms import *
from django.views.generic import *
from django.core.context_processors import csrf
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import json
import django.utils.simplejson as simplejson

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def RecipeList(request):
	if request.user.is_authenticated():
	
		user = request.user
		recipes = Recipe.objects.filter(created_by = user)
		
		return render_to_response("recipe/recipe_list.html", {
			"recipes": recipes,
			"user": user,
		}, context_instance=RequestContext(request))
	else:
		#redirectUrl = "/login/"
		#return redirect(redirectUrl)
		return render_to_response("recipe/recipe_list.html", {
			"user": user,
		}, context_instance=RequestContext(request))
		
		
def RecipeEdit(request, slug):
    VersionFormSet = VersionForm
    StepFormSet = formset_factory(StepForm)
    IngredientFormSet = formset_factory(IngredientForm)
    version_list = ""
    versionSetAll = ""    
    versionSetLatest = ""
    form = {}
    ingredient_formset = {}
    step_formset = {}
    slugValue = slug
    container = Recipe.objects.get(slug = slugValue)

	
    if request.POST:
    	version_container = container.id
    	version_form = VersionFormSet
	c = {}
	c.update(csrf(request))
        form = version_form(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("recipe/recipe_detail.html", {
            	"container": container,
            	"version": container.version_set.latest(field_name='id'),
            	"version_list": container.version_set.all(),
            	#        "steps": container.steps,
            	#        "test": version_form,
            	"version_form": version_form,
    			}, context_instance=RequestContext(request))
    else:
	c = {}
	c.update(csrf(request))
        version_container = container.id
        version_form = VersionFormSet(initial = {'recipe': version_container})
        version_list = ""
        versionSet = ""
#       version_id = container.version_set.latest('id')
#        form = VersionForm(initial={'Recipe': version_container})
#        ingredient_formset = IngredientFormSet(instance=Version(), initial={"Recipe": version_id})
#    	step_formset = StepFormSet(instance=Version())
        container = Recipe.objects.get(slug = slugValue)
        try:
        	versionSetAll = container.version_set.all()
        	versionSetLatest = container.version_set.latest(field_name='id')
        except container.version_set.DoesNoteExist:
        	versionSet = None     
    return render_to_response("recipe/container_detail.html", {
#        "form": form,
#        "ingredient_formset": ingredient_formset,
#        "step_formset": step_formset,
        "container": container,
        "version": versionSetLatest,
        "version_list": versionSetAll,
#        "steps": container.steps,
#        "test": version_form,
		"version_form": version_form,
    }, context_instance=RequestContext(request))
    
    
    
def RecipeAdd(request):
	testUser = request.user
	VersionFormSet = VersionForm
	RecipeFormSet = RecipeForm
#	VersionFormSet = inlineformset_factory(Recipe, Version, max_num=1)	
    
	if request.POST:
		c = {}
		c.update(csrf(request))
		postData = request.POST.copy()
		
		recipe_form = RecipeFormSet(request.POST)
		if recipe_form.is_valid():
			new_recipe = recipe_form.save(commit=False)
			new_recipe.slug = slugify(new_recipe.title)
			recipe_id = new_recipe.id
			new_recipe.created_by = testUser
			new_recipe.save()
			postData['recipe'] = new_recipe.id
			postData['Note'] = "First Version"
			version_formset = VersionFormSet(postData)
			#request.POST['recipe'] = new_recipe.id
			if version_formset.is_valid():
				#version = version_formset.save(commit=False)
				#version.cleaned_data['recipe'] = new_recipe
				version_formset.save()

			
			
			
				redirectUrl = "/recipe/" + new_recipe.slug
				return redirect(redirectUrl)
				
			else:
				recipe_form_errors = recipe_form.errors
				version_form_errors = version_formset.errors
				testMessage = request.POST
				return render_to_response('recipe/add.html', {'recipe_form': RecipeFormSet(),'test': testMessage, 'version_formset': VersionFormSet(), 'version_form_errors': version_form_errors, 'recipe_form_errors': recipe_form_errors}, context_instance=RequestContext(request))

		else:
			recipe_form_errors = recipe_form.errors
			#version_form_errors = version_form.errors
			testMessage = request.POST
			return render_to_response('recipe/add.html', {'recipe_form': RecipeFormSet(),'test': testMessage, 'version_formset': VersionFormSet(), 'recipe_form_errors': recipe_form_errors}, context_instance=RequestContext(request))
					
		return redirect('/')
		#return HttpResponseRedirect(reverse('recipe:RecipeEdit', args=(request, slug)))
		
	
	else:
		c = {}
		c.update(csrf(request))
		recipe_form = RecipeFormSet()
		version_formset = VersionFormSet()	
		
		return render_to_response("recipe/add.html", {
			"recipe_form": recipe_form,
			"version_form": version_formset,
			"test": testUser,
		}, context_instance=RequestContext(request))

def Profile(request):

	profileUser = request.user
	
	return render_to_response("registration/profile.html", {
		"user": profileUser
	}, context_instance=RequestContext(request))