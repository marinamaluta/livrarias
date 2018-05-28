from django.shortcuts import render
from django.http import HttpResponse
from conteudos.models import Material, TEMA, TIPO


# Create your views here.
def index(request):
    _template = 'conteudos/home.html'
    temas = TEMA.objects.all()
    tipos = TIPO.objects.all()
    _args = {'temas': temas, 'tipos': tipos, 'request': request}
    return render(request, template_name=_template, context=_args)

def tipo(request, x):
    _template = 'conteudos/tipo.html'
    _tipo = TIPO.objects.get(id=x)
    _items = Material.objects.filter(tipo=_tipo)
    _args = {'items': _items, 'tipo': _tipo}
    return render(request, template_name=_template, context=_args)

def estatisticas(request):
    _template = 'conteudos/estatisticas.html'
    valores = {}
    t = TIPO.objects.all()
    for _tipo in t:
        valores[_tipo.tipo] = (len(Material.objects.filter(tipo=_tipo)), _tipo.img_material_tipo)

    cores = ['red', 'blue', 'green', 'purple']
    _args = {'valores': valores, 'cores': cores, 't': t}
    return render(request, template_name=_template, context=_args)

def tema(request, x):
    _template = 'conteudos/tema.html'
    tema = TEMA.objects.get(id=x)
    materiais = Material.objects.filter(tema=tema)
    db_tipo = TIPO.objects.all()
    vid = ''
    site = ''
    try:
        video_tema_id = tema.video_tema_id
        vid = video_tema_id.split('_')[1]
        site = video_tema_id.split('_')[0]
    except:
        pass
    tipo = {}
    tipo_img = {}
    for t in materiais:
        tipo[t.tipo.tipo] = t.tipo.id
        tipo_img[t.tipo.tipo] = t.tipo.img_material_tipo

    _args = {'tema': tema, 'tipo': tipo, 'x': x, 'tipo_img': tipo_img, 'vid':vid, 'site':site}
    return render(request, template_name=_template, context=_args)

def tema_tipo(request, x, tipo):
    _template = 'conteudos/tema-tipo.html'
    tema = TEMA.objects.get(id=x)
    tipo = TIPO.objects.get(id=tipo)
    materiais = Material.objects.filter(tema=tema, tipo=tipo)
    _args = {'tema': tema, 'materiais': materiais}
    return render(request, template_name=_template, context=_args)
