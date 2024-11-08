from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path
from . import views
from .views import *

app_name='followup'

urlpatterns = [
    path('pn/', login_required(PadronView.as_view()), name='sello'),
    path('pn/filterDist/', views.DistrictView.as_view(), name='filter_dist'),
    path('pn/list/', views.ListSello.as_view(), name='list_sello'),
    path('pn/print/', views.PrintSello.as_view(), name='print_sello'),
    path('pn/actas/', ActasView.as_view(), name='actas'),
    path('pn/padronNom/', PrintPadronNom.as_view(), name='padron_nom'),
    path('plano/', login_required(PlanoView.as_view()), name='plano'),
    path('plano/filterDist/', DistrictView.as_view(), name='filter_dist'),
    path('plano/filterEstab/', views.EESS.as_view(), name='filter_eess'),
    path('plano/print/', PrintPlano.as_view(), name='plano_print'),
]