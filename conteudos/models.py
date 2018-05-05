from django.db import models

from django.utils import timezone
from django.utils.html import escape, mark_safe

class ODS(models.Model):
    codigo = models.CharField(max_length=50, verbose_name='Código')
    desc = models.CharField(max_length=300, blank=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.codigo)


class TIPO(models.Model):
    tipo = models.CharField(max_length=50, verbose_name='Tipo')

    def __str__(self):
        return str(self.tipo)

class BNCC(models.Model):
    codigo = models.CharField(max_length=50, verbose_name='Código')
    desc = models.CharField(max_length=300, blank=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.codigo)


class PUBLICOALVO(models.Model):
    publico = models.CharField(max_length=50, verbose_name='Público-alvo')

    def __str__(self):
        return str(self.publico)


class FAIXAETARIA(models.Model):
    faixa = models.CharField(max_length=50, verbose_name='Faixa Etaria')

    def __str__(self):
        return str(self.faixa)


class OBJETIVOS(models.Model):
    objetivo = models.CharField(max_length=250, verbose_name='Objetivo')

    def __str__(self):
        return str(self.objetivo)


class Material(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    desc = models.TextField(max_length=1000, blank=True, verbose_name='Descrição do Título')
    tipo = models.ManyToManyField(TIPO, blank=True, verbose_name='Tipo')
    ods = models.ManyToManyField(ODS, blank=True, verbose_name='ODS')
    publico_alvo = models.ManyToManyField(PUBLICOALVO, blank=True, verbose_name='Público-alvo')
    faixa_etaria = models.ManyToManyField(FAIXAETARIA, blank=True, verbose_name='Faixa Etaria')
    competencia_bncc = models.ManyToManyField(BNCC, blank=True, verbose_name='Competência BNCC')
    preco = models.CharField(max_length=15, blank=True, verbose_name='Preço')
    objetivos = models.ManyToManyField(OBJETIVOS, blank=True, verbose_name='Objetivos')
    link = models.URLField(blank=True, verbose_name='Link de acesso ao material')
    link_venda =  models.URLField(blank=True, verbose_name='Link de acesso material para venda')

    def __str__(self):
        return str(self.titulo)