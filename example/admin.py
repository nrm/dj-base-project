from example.models import Sample
from django.contrib import admin


from django import forms
from ckeditor.widgets import CKEditor


#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class SampleForm(forms.ModelForm):
    another_body = forms.CharField( widget=CKEditor(ckeditor_config='full'))
    #plain_body = forms.CharField( widget=CKEditor(ckeditor_config='simple_toolbar'))
    plain_body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Sample


class SampleAdmin(admin.ModelAdmin):
    form = SampleForm


admin.site.register(Sample, SampleAdmin)
