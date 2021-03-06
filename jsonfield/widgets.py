from django import forms
from django.utils import simplejson as json
from django.conf import settings

import jsonfield.fields

class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ""
        if not isinstance(value, basestring):
            value = json.dumps(value, indent=2, default=jsonfield.fields.default)
        return super(JSONWidget, self).render(name, value, attrs)


class JSONSelectWidget(forms.SelectMultiple):
    pass
