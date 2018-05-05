from django.shortcuts import render
from django.http import HttpResponse
from conteudos.models import Material


# Create your views here.
def index(request):
    _template = 'conteudos/home.html'
    materiais = Material.objects.all()
    _args = {'materiais': materiais}
    return render(request, template_name=_template, context=_args)