from django.shortcuts import render
from django.http import HttpResponse
from conteudos.models import Material, TEMA, TIPO


# Create your views here.
def index(request):
    _template = 'conteudos/home.html'
    materiais = Material.objects.all()
    temas = TEMA.objects.all()
    _args = {'materiais': materiais, 'temas': temas}
    return render(request, template_name=_template, context=_args)


def tema(request, x):
    _template = 'conteudos/tema.html'
    tema = TEMA.objects.get(id=x)
    materiais = Material.objects.filter(tema=tema)
    db_tipo = TIPO.objects.all()

    tipo = {}
    tipo_img = {}
    for t in materiais:
        tipo[t.tipo.tipo] = t.tipo.id
        tipo_img[t.tipo.tipo] = t.tipo.img_material_tipo

    _args = {'tema': tema, 'tipo': tipo, 'x': x, 'tipo_img': tipo_img}
    return render(request, template_name=_template, context=_args)

def tema_tipo(request, x, tipo):
    _template = 'conteudos/tema-tipo.html'
    tema = TEMA.objects.get(id=x)
    tipo = TIPO.objects.get(id=tipo)
    materiais = Material.objects.filter(tema=tema, tipo=tipo)
    _args = {'tema': tema, 'materiais': materiais}
    return render(request, template_name=_template, context=_args)