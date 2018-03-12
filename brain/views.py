from django.http import HttpResponse
from .models import *
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

def signUpLogIn(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))