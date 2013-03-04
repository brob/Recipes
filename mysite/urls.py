from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipe.models import *
from recipe.views import *
from django.views.generic import *
from django.http import HttpResponse

from recipe.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()


info_dict = {
    'queryset': Recipe.objects.all(),
}

urlpatterns = patterns('',
    # Examples:
    url(r'^recipe/$', RecipeList),
    url(r'^recipes/$', RecipeList),
   	url(r'^recipe/add/', RecipeAdd), 
	url(r'^recipe/(?P<slug>[-_\w]+)/$', RecipeEdit),
	url(r'^recipe/(?P<slug>[-_\w]+)/edit/$', RecipeEdit),
	#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r"^account/", include("account.urls")),
	(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^accounts/profile/', Profile),
	
	
    # url(r'^mysite/', include('mysite.foo.urls')),
    #url(r'^$', ArticleListView.as_view(), name='article-list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
)