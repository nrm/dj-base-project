# Create your views here.
from django.shortcuts import render_to_response
from example.models import Sample
from django.template import RequestContext


def test(request):
    #posts = Sample.objects.all()
    posts ='test text'

    return render_to_response('index.html', {'posts': posts},
            context_instance=RequestContext(request))

