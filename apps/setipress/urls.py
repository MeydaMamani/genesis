from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path
from .views import *

app_name='setipress'

urlpatterns = [
    path('', login_required(SetiIpressView.as_view()), name='setipress'),
    path('filterDist/', Districts.as_view(), name='filter_dist'),
    path('filterEstab/', EESS.as_view(), name='filter_dist'),
    path('print/', PrintTxt.as_view(), name='print'),
]