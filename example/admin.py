from example.models import Sample
from django.contrib import admin


from django import forms
#from ckeditor.widgets import CKEditor


from tinymce.widgets import TinyMCE
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse


#class CommonMedia:
#    js = (
#        'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
#        '%sjs/editor.js'%STATIC_URL,
#        )
#    css = {
#        #'all': ('%scss/editor.css'%STATIC_URL,),
#        #'all': ('/site_media/css/editor.css',),
#        }
#

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class SampleForm(forms.ModelForm):
    #another_body = forms.CharField( widget=CKEditor(ckeditor_config='full'))
    another_body = forms.CharField(widget=TinyMCE())
    #plain_body = forms.CharField( widget=CKEditor(ckeditor_config='simple_toolbar'))
    plain_body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Sample


class SampleAdmin(admin.ModelAdmin):
    form = SampleForm


admin.site.register(Sample, SampleAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
