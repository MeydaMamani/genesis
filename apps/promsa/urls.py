from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path
from . import views
from .views import *

app_name='promsa'

urlpatterns = [
    path('', login_required(PromsaView.as_view()), name='promsa'),
    path('filterDist/', views.Districts.as_view(), name='filter_dist'),
    path('filterEstab/', views.EESS.as_view(), name='filter_dist'),
    path('print/', PrintPromsa.as_view(), name='print'),
]