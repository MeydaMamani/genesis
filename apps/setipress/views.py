from django.views.generic import TemplateView, View
from django.core import serializers
from django.http import JsonResponse, HttpResponse, QueryDict
from .models import b1, b2
from apps.main.models import Sector, Provincia, Distrito, Establecimiento

# library excel
from openpyxl import Workbook


class SetiIpressView(TemplateView):
    template_name = 'index2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['provincia'] = Provincia.objects.exclude(codigo__in=['00'])
        return context


class Districts(View):
    def get(self, request, *args, **kwargs):
        dist = serializers.serialize('json', Distrito.objects.filter(prov_id=request.GET['id']), indent=2, use_natural_foreign_keys=True)
        return HttpResponse(dist, content_type='application/json')


class EESS(View):
    def get(self, request, *args, **kwargs):
        eess = serializers.serialize('json', Establecimiento.objects.filter(dist_id=request.GET['id'], sector_id=7), indent=2, use_natural_foreign_keys=True)
        return HttpResponse(eess, content_type='application/json')


class PrintTxt(View):
    def get(self, request, *args, **kwargs):
        if request.GET['tipo'] == 'tb1':
            if request.GET['eess'] == 'TODOS':
                tramab1 = b1.objects.filter(cod_dist=request.GET['dist'], anio=request.GET['anio'], mes=request.GET['mes'])
                trb0 = b1.objects.filter(cod_dist=request.GET['dist'], anio=request.GET['anio'], mes=request.GET['mes']).first()
                ipress = trb0.cod_dist2
            else:
                tramab1 = b1.objects.filter(cod_eess=request.GET['eess'], anio=request.GET['anio'], mes=request.GET['mes'])
                trb1 = b1.objects.filter(cod_eess=request.GET['eess'], anio=request.GET['anio'], mes=request.GET['mes']).first()
                ipress = trb1.cod_ipress

            contenido = ''
            for tb1 in tramab1:
                ugipress = tb1.cod_ugipress
                contenido += f"{tb1.periodo}|{tb1.cod_ipress}|{tb1.cod_ugipress}|{tb1.sexo}|{tb1.gedad}|{tb1.aten_med}|{tb1.aten_nomed}|{tb1.aten_mes}\n"

            contenido = contenido.rstrip('\n')
            nombre_archivo = f"{ugipress}_{ipress}_{request.GET['anio']}_{request.GET['mes']}_TAB1.txt"
            response = HttpResponse(contenido, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'

        elif request.GET['tipo'] == 'tb2':
            if request.GET['eess'] == 'TODOS':
                tramab2 = b2.objects.filter(cod_dist=request.GET['dist'], anio=request.GET['anio'], mes=request.GET['mes'])
                trb0 = b2.objects.filter(cod_dist=request.GET['dist'], anio=request.GET['anio'], mes=request.GET['mes']).first()
                ipress = trb0.cod_dist2
            else:
                tramab2 = b2.objects.filter(cod_eess=request.GET['eess'], anio=request.GET['anio'], mes=request.GET['mes'])
                trb2 = b1.objects.filter(cod_eess=request.GET['eess'], anio=request.GET['anio'], mes=request.GET['mes']).first()
                ipress = trb2.cod_ipress

            contenido2 = ''
            for tb2 in tramab2:
                ugipress = tb2.cod_ugipress
                contenido2 += f"{tb2.periodo}|{tb2.cod_ipress}|{tb2.cod_ugipress}|{tb2.sexo}|{tb2.gedad}|{tb2.dx_def}|{tb2.aten}\n"

            contenido2 = contenido2.rstrip('\n')
            nombre_archivo = f"{ugipress}_{ipress}_{request.GET['anio']}_{request.GET['mes']}_TAB2.txt"
            response = HttpResponse(contenido2, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'

        return response
