from django.http import JsonResponse, HttpResponse, QueryDict
from django.core import serializers

from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, View

# Create your views here.
class OperacionalView(TemplateView):
    template_name = 'operacionales/index.html'


class DesaView(TemplateView):
    template_name = 'desa/index.html'


class ProgramasView(TemplateView):
    template_name = 'programas/index2.html'
