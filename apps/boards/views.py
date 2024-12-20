from django.http import JsonResponse, HttpResponse, QueryDict
from django.core import serializers
import json
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, View

from apps.main.models import Sector, Provincia, Distrito, Establecimiento
from apps.boards.models import fedninio, fedgestante
from django.db.models import Sum, FloatField, F, ExpressionWrapper, Q, DecimalField
from django.db.models.functions import Cast, Round

# Create your views here.
class OperacionalView(TemplateView):
    template_name = 'operacionales/index.html'


class DesaView(TemplateView):
    template_name = 'desa/index.html'


class ProgramasView(TemplateView):
    template_name = 'programas/index2.html'


class FedView(TemplateView):
    template_name = 'fed/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['provincia'] = Provincia.objects.exclude(codigo__in=['00'])
        return context


class DistrictView(View):
    def get(self, request, *args, **kwargs):
        dist = serializers.serialize('json', Distrito.objects.filter(prov_id=request.GET['id']).order_by('nombre'), indent=2, use_natural_foreign_keys=True)
        return HttpResponse(dist, content_type='application/json')


class FedChild(View):
    def get(self, request, *args, **kwargs):
        if request.GET['prov'] == 'TODOS':
            resChild = fedninio.objects.filter(Q(anio=2024, mes__in=[10, 11, 12]) | Q(anio=2025, mes__in=[1,2])).values('anio','mes','cod_dep','departamento','nombremes').annotate(
                        av_pqtrn=Round(ExpressionWrapper(Cast(Sum('num_prn'), output_field=FloatField()) / Cast(Sum('den_prn'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0201=Round(ExpressionWrapper(Cast(Sum('num_si0201'), output_field=FloatField()) / Cast(Sum('den_si0201'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0202=Round(ExpressionWrapper(Cast(Sum('num_si0202'), output_field=FloatField()) / Cast(Sum('den_si0202'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0203=Round(ExpressionWrapper(Cast(Sum('num_si0203'), output_field=FloatField()) / Cast(Sum('den_si0203'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si03=Round(ExpressionWrapper(Cast(Sum('num_si03'), output_field=FloatField()) / Cast(Sum('den_si03'), output_field=FloatField()) * 100, output_field=FloatField()), 1)
                    ).order_by('anio', 'mes', 'cod_dep')

        elif request.GET['prov'] != 'TODOS' and request.GET['dist'] == 'TODOS':
            resChild = fedninio.objects.filter(Q(cod_prov=request.GET['prov']) & ((Q(anio=2024) & Q(mes__in=[10, 11, 12])) | (Q(anio=2025) & Q(mes__in=[1, 2, 3])))
                        ).values('anio', 'mes', 'cod_dep', 'departamento', 'nombremes').annotate(
                        av_pqtrn=Round(ExpressionWrapper(Cast(Sum('num_prn'), output_field=FloatField()) / Cast(Sum('den_prn'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0201=Round(ExpressionWrapper(Cast(Sum('num_si0201'), output_field=FloatField()) / Cast(Sum('den_si0201'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0202=Round(ExpressionWrapper(Cast(Sum('num_si0202'), output_field=FloatField()) / Cast(Sum('den_si0202'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0203=Round(ExpressionWrapper(Cast(Sum('num_si0203'), output_field=FloatField()) / Cast(Sum('den_si0203'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si03=Round(ExpressionWrapper(Cast(Sum('num_si03'), output_field=FloatField()) / Cast(Sum('den_si03'), output_field=FloatField()) * 100, output_field=FloatField()), 1),).order_by('anio', 'mes', 'cod_dep')

        elif request.GET['prov'] != 'TODOS' and request.GET['dist'] != 'TODOS':
            resChild = fedninio.objects.filter(Q(cod_dist=request.GET['dist']) & ((Q(anio=2024) & Q(mes__in=[10, 11, 12])) | (Q(anio=2025) & Q(mes__in=[1, 2, 3])))
                        ).values('anio', 'mes', 'cod_dep', 'departamento', 'nombremes').annotate(
                        av_pqtrn=Round(ExpressionWrapper(Cast(Sum('num_prn'), output_field=FloatField()) / Cast(Sum('den_prn'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0201=Round(ExpressionWrapper(Cast(Sum('num_si0201'), output_field=FloatField()) / Cast(Sum('den_si0201'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0202=Round(ExpressionWrapper(Cast(Sum('num_si0202'), output_field=FloatField()) / Cast(Sum('den_si0202'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si0203=Round(ExpressionWrapper(Cast(Sum('num_si0203'), output_field=FloatField()) / Cast(Sum('den_si0203'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si03=Round(ExpressionWrapper(Cast(Sum('num_si03'), output_field=FloatField()) / Cast(Sum('den_si03'), output_field=FloatField()) * 100, output_field=FloatField()), 1),).order_by('anio', 'mes', 'cod_dep')

        return HttpResponse(json.dumps(list(resChild)), content_type='application/json')


class FedGest(View):
    def get(self, request, *args, **kwargs):
        if request.GET['prov'] == 'TODOS':
            resGest = fedgestante.objects.filter(Q(anio=2024, mes__in=[10, 11, 12]) | Q(anio=2025, mes__in=[1,2])).values('anio','mes','cod_dep','departamento','nombremes').annotate(
                        av_si01=Round(ExpressionWrapper(Cast(Sum('num_si01'), output_field=FloatField()) / Cast(Sum('den_si01'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si04=Round(ExpressionWrapper(Cast(Sum('num_si04'), output_field=FloatField()) / Cast(Sum('den_si04'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vi0101=Round(ExpressionWrapper(Cast(Sum('num_vi0101'), output_field=FloatField()) / Cast(Sum('den_vi0101'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vi0102=Round(ExpressionWrapper(Cast(Sum('num_vi0102'), output_field=FloatField()) / Cast(Sum('den_vi0102'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vii01=Round(ExpressionWrapper(Cast(Sum('num_vii01'), output_field=FloatField()) / Cast(Sum('den_vii01'), output_field=FloatField()) * 100, output_field=FloatField()), 1)
                    ).order_by('anio', 'mes', 'cod_dep')

        elif request.GET['prov'] != 'TODOS' and request.GET['dist'] == 'TODOS':
            resGest = fedgestante.objects.filter(Q(cod_prov=request.GET['prov']) & ((Q(anio=2024) & Q(mes__in=[10, 11, 12])) | (Q(anio=2025) & Q(mes__in=[1, 2, 3])))
                        ).values('anio', 'mes', 'cod_dep', 'departamento', 'nombremes').annotate(
                        av_si01=Round(ExpressionWrapper(Cast(Sum('num_si01'), output_field=FloatField()) / Cast(Sum('den_si01'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si04=Round(ExpressionWrapper(Cast(Sum('num_si04'), output_field=FloatField()) / Cast(Sum('den_si04'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vi0101=Round(ExpressionWrapper(Cast(Sum('num_vi0101'), output_field=FloatField()) / Cast(Sum('den_vi0101'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vi0102=Round(ExpressionWrapper(Cast(Sum('num_vi0102'), output_field=FloatField()) / Cast(Sum('den_vi0102'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vii01=Round(ExpressionWrapper(Cast(Sum('num_vii01'), output_field=FloatField()) / Cast(Sum('den_vii01'), output_field=FloatField()) * 100, output_field=FloatField()), 1),).order_by('anio', 'mes', 'cod_dep')

        elif request.GET['prov'] != 'TODOS' and request.GET['dist'] != 'TODOS':
            resGest = fedgestante.objects.filter(Q(cod_dist=request.GET['dist']) & ((Q(anio=2024) & Q(mes__in=[10, 11, 12])) | (Q(anio=2025) & Q(mes__in=[1, 2, 3])))
                        ).values('anio', 'mes', 'cod_dep', 'departamento', 'nombremes').annotate(
                        av_si01=Round(ExpressionWrapper(Cast(Sum('num_si01'), output_field=FloatField()) / Cast(Sum('den_si01'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_si04=Round(ExpressionWrapper(Cast(Sum('num_si04'), output_field=FloatField()) / Cast(Sum('den_si04'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vi0101=Round(ExpressionWrapper(Cast(Sum('num_vi0101'), output_field=FloatField()) / Cast(Sum('den_vi0101'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vi0102=Round(ExpressionWrapper(Cast(Sum('num_vi0102'), output_field=FloatField()) / Cast(Sum('den_vi0102'), output_field=FloatField()) * 100, output_field=FloatField()), 1),
                        av_vii01=Round(ExpressionWrapper(Cast(Sum('num_vii01'), output_field=FloatField()) / Cast(Sum('den_vii01'), output_field=FloatField()) * 100, output_field=FloatField()), 1),).order_by('anio', 'mes', 'cod_dep')

        return HttpResponse(json.dumps(list(resGest)), content_type='application/json')


class CoberturasView(TemplateView):
    template_name = 'coberturas/index.html'
