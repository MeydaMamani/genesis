from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

app_name="boards"

urlpatterns = [
    path('operacional/', login_required(views.OperacionalMinsaView.as_view()), name='operacional'),
    path('desa/', login_required(views.DesaView.as_view()), name='desa'),
]