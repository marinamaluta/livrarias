from django.db import models

from django.utils import timezone
from django.utils.html import escape, mark_safe

class ODS(models.Model):
    codigo = models.CharField(max_length=50, verbose_name='Código')
    desc = models.CharField(max_length=300, blank=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.codigo)
       
    class Meta:
        verbose_name = "ODS"
        verbose_name_plural = "ODS"


class TIPO(models.Model):
    tipo = models.CharField(max_length=50, verbose_name='Tipo')
    img_material_tipo = models.CharField(max_length=100, blank=True, default='', verbose_name='Img do material tipo')

    def __str__(self):
        return str(self.tipo)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipo"

class BNCC(models.Model):
    codigo = models.CharField(max_length=50, verbose_name='Código')
    desc = models.CharField(max_length=300, blank=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.codigo)

    class Meta:
        verbose_name = "BNCC"
        verbose_name_plural = "BNCC"

class PUBLICOALVO(models.Model):
    publico = models.CharField(max_length=50, verbose_name='Público-alvo')

    def __str__(self):
        return str(self.publico)

    class Meta:
        verbose_name = "Público-alvo"
        verbose_name_plural = "Público-alvo"

class FAIXAETARIA(models.Model):
    faixa = models.CharField(max_length=50, verbose_name='Faixa Etaria')

    def __str__(self):
        return str(self.faixa)

    class Meta:
        verbose_name = "Faixa-etária"
        verbose_name_plural = "Faixa-etária"

class OBJETIVOS(models.Model):
    objetivo = models.CharField(max_length=250, verbose_name='Objetivo')

    def __str__(self):
        return str(self.objetivo)

    class Meta:
        verbose_name = "Objetivos"
        verbose_name_plural = "Objetivos"

class TEMA(models.Model):
    tema = models.CharField(max_length=250, verbose_name='Tema')
    subtema = models.CharField(max_length=350, default='', blank=True, verbose_name='Subtema')
    img_tema = models.CharField(max_length=25, default='', verbose_name='Nome da Img Tema')
    video_tema_id = models.CharField(max_length=100, blank=True, default='', verbose_name='Video do tema')


    def __str__(self):
        return str(self.tema)

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Tema"


class Material(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Descrição do Título')
    tipo = models.ForeignKey(TIPO, on_delete=models.CASCADE, default='', verbose_name='Tipo')
    ods = models.ManyToManyField(ODS, blank=True, verbose_name='ODS')
    publico_alvo = models.ManyToManyField(PUBLICOALVO, blank=True, verbose_name='Público-alvo')
    faixa_etaria = models.ManyToManyField(FAIXAETARIA, blank=True, verbose_name='Faixa Etaria')
    tema = models.ForeignKey(TEMA, blank=False, on_delete=models.CASCADE, verbose_name='Tema')
    competencia_bncc = models.ManyToManyField(BNCC, blank=True, verbose_name='Competência BNCC')
    preco = models.CharField(max_length=15, blank=True, verbose_name='Preço')
    objetivos = models.ManyToManyField(OBJETIVOS, blank=True, verbose_name='Objetivos')
    link = models.URLField(blank=True, verbose_name='Link de acesso ao material')
    link_venda =  models.URLField(blank=True, verbose_name='Link de acesso material para venda')
    imagem_capa = models.URLField(blank=True, verbose_name='URL da imagem de capa')


    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

    def __str__(self):
        return str(self.titulo)

    def h(self, tag):
        code = '<span class="badge badge-primary" style="background-color:rgb(232,232,232,0.9); color: #392779; ">%s</span>' % (tag)
        return code

    def tags(self):
        html = ''
        for item in self.ods.all():
            html += self.h(item.codigo)
        for item in self.publico_alvo.all():
            html += self.h(item.publico)
        for item in self.competencia_bncc.all():
            html += self.h(item.codigo)

        return mark_safe(html)
