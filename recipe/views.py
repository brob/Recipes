# Create your views here.
from django.http import HttpResponse
import datetime
from recipe.models import *
from django.forms import *
from django.views.generic import *
from django.core.context_processors import csrf
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
import django.utils.simplejson as simplejson

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
class RecipeList(ListView):
	
	model = Recipe
	
	def get_context_data(self, **kwargs):
		context = super(RecipeList, self).get_context_data(**kwargs)
#		context['now'] = timezone.now()
		return context

class RecipeDetail(DetailView):
	model = Recipe



	def get_context_data(self, **kwargs):
		context = super(RecipeDetail, self).get_context_data(**kwargs)
		version_container = context['container'].id
		version_form = VersionForm(initial={'Recipe': version_container})
		IngredientInlineFormSet = IngredientFormSet
		StepInlineFormSet = StepFormSet   
	
		context['version_form'] = version_form
		context['ingredient_form'] = IngredientInlineFormSet
		context['step_form'] = StepInlineFormSet
		#context['test'] = StepInlineFormSet
		return context
		
def RecipeEdit(request, slug):
    form = {}
    ingredient_formset = {}
    step_formset = {}
    slugValue = slug
    container = Recipe.objects.get(slug = slugValue)

    if request.POST:
	c = {}
	c.update(csrf(request))
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save()
            ingredient_formset = IngredientFormSet(request.POST)
            if ingredient_formset.is_valid():
                version.save()
                ingredient_formset.save(commit=False)
            step_formset = StepFormSet(request.POST)
            if step_formset.is_valid():
            	version.save()
            	ingredient_formset.save()
            	step_formset.save()        
                return render_to_response("recipe/container_detail.html", {
        			"form": form,
        			"ingredient_formset": ingredient_formset,
        			"step_formset": step_formset,
        			"container": container
    			}, context_instance=RequestContext(request))
    else:
	c = {}
	c.update(csrf(request))
        version_container = container.id
 #       version_id = container.version_set.latest('id')
#        form = VersionForm(initial={'Recipe': version_container})
#        ingredient_formset = IngredientFormSet(instance=Version(), initial={"Recipe": version_id})
#    	step_formset = StepFormSet(instance=Version())
        container = Recipe.objects.get(slug = slugValue)
    return render_to_response("recipe/container_detail.html", {
#        "form": form,
#        "ingredient_formset": ingredient_formset,
#        "step_formset": step_formset,
        "container": container,
        "version": container.version_set.latest(field_name='id'),
        "version_list": container.version_set.all().reverse(),
#        "steps": container.steps,
#        "test": simplejson.loads('[%s]' % json.dumps(container.ingredients)[:-1]),
    }, context_instance=RequestContext(request))