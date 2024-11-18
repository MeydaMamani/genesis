
from django.http import JsonResponse, HttpResponse, QueryDict
from django.core import serializers

from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, View

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect

from datetime import date, datetime
from django.db import connection
import json
import locale
from apps.followup.models import plano

# library excel
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side, Color
# from apps.main.models import Departamento, Provincia, Distrito, Establecimiento

User = get_user_model()
from apps.person.models import Person
from .forms import LoginForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard:dash')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    #verifica la petición
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        try:
            ObjPerson = Person.objects.get(pk=user.id_person.id)
            ObjUser = User.objects.get(pk=user.pk)
            # if ObjUser.type_ca == 'CA':
            #     name_ca = Establecimiento.objects.get(codigo=ObjUser.code_ca)
            # elif ObjUser.type_ca == 'DS':
            #     name_ca = Distrito.objects.get(codigo=ObjUser.code_ca)
            # elif ObjUser.type_ca == 'PR':
            #     name_ca = Provincia.objects.get(codigo=ObjUser.code_ca)
            # elif ObjUser.type_ca == 'DP':
            #     name_ca = Departamento.objects.get(codigo=ObjUser.code_ca)

            self.request.session['sytem'] = { 'full_name': ObjPerson.last_name0+' '+ObjPerson.last_name1+', '+ObjPerson.names.title(),
                                            'doc': ObjPerson.pdoc }
                                            # 'typeca': ObjUser.type_ca, 'codeca': ObjUser.code_ca, 'nombreca': name_ca.nombre }

        except:
            print("Hay un error en los valores de entrada")

        return super(LoginView, self).form_valid(form)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')


class DashView(TemplateView):
    template_name = 'dash.html'


class SearchView(View):
    def get(self, request, *args, **kwargs):
        data_get = kwargs['information']
        data = plano.objects.filter(doc_pacien=data_get).order_by('-fec_aten').values('id_cita', 'eess', 'lote', 'num_pag',
                'doc_pacien','fnac_pacien', 'edad_reg', 'fec_aten','tdiag','codigo','vlab','id_corr_lab','fur','grupo_edad')
        sql_query = """ SELECT DISTINCT pl.doc_pacien, 1 as id, pl.fnac_pacien, pl.nombres_pacien, pl.genero, pr.programa
                        FROM BD_GENESIS_V2.dbo.followup_plano pl LEFT JOIN BD_GENESIS_V2.dbo.programas pr
                        ON pl.doc_pacien = pr.NUMERO_DE_DOCUMENTO_DEL_NINO WHERE pl.doc_pacien = %s"""
        user = plano.objects.raw(sql_query, [data_get])
        data_user = {'person': list(data), 'data_get': list(set(user)), 'load': len(user)}
        return render(request, 'search/index.html', data_user)
