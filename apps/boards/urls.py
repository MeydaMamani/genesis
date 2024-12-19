from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

app_name="boards"

urlpatterns = [
    path('operacional/', login_required(views.OperacionalView.as_view()), name='operacional'),
    path('desa/', login_required(views.DesaView.as_view()), name='desa'),
    path('prog/', login_required(views.ProgramasView.as_view()), name='programs'),
    # path('fed/', login_required(views.FedView.as_view()), name='fed'),
    # path('fed/child/', login_required(views.FedChild.as_view()), name='fed'),
    # path('fed/filterDist/', login_required(views.DistrictView.as_view()), name='filter_dist'),
    path('cobertura/', login_required(views.CoberturasView.as_view()), name='cobertura'),
]