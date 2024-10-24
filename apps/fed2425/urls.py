from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path
from . import views
from .views import *

app_name='fed2425'

urlpatterns = [
    path('mc03/', login_required(MC03View.as_view()), name='mc03'),
    path('mc03/filterDist/', views.DistrictView.as_view(), name='filter_dist'),
    path('mc03/list/', ListMC03.as_view(), name='mc03_list'),
    path('mc03/print/', PrintMC03.as_view(), name='mc03_print'),
    path('si01/', login_required(SI01View.as_view()), name='si01'),
    path('si01/filterDist/', views.DistrictSIView.as_view(), name='filter_dist'),
    path('si01/list/', ListSI01.as_view(), name='si01_list'),
    path('si01/print/', PrintSI01.as_view(), name='mc03_print'),
    path('si0201/', login_required(SI0201View.as_view()), name='si0201'),
    path('si0201/filterDist/', views.DistrictSIView.as_view(), name='filter_dist'),
    path('si0201/list/', ListSI0201.as_view(), name='si0201_list'),
    path('si0201/print/', PrintSI0201.as_view(), name='si0201_print'),
    path('si0202/', login_required(SI0202View.as_view()), name='si0202'),
    path('si0202/list/', ListSI0202.as_view(), name='si0202_list'),
    path('si0202/filterDist/', views.DistrictSI0202View.as_view(), name='filter_dist'),
    path('si0202/print/', PrintSI0202.as_view(), name='si0202_print'),
    path('si0203/', login_required(SI0203View.as_view()), name='si0203'),
    path('si0203/list/', ListSI0203.as_view(), name='si0203_list'),
    path('si0203/filterDist/', views.DistrictSI0203View.as_view(), name='filter_dist'),
    path('si0203/print/', PrintSI0203.as_view(), name='si0203_print'),
    path('si0401/', login_required(SI0401View.as_view()), name='si0401'),
    path('si0401/list/', ListSI0401.as_view(), name='si0401_list'),
    path('si0401/filterDist/', views.DistrictSI0401View.as_view(), name='filter_dist'),
    path('si0401/print/', PrintSI0401.as_view(), name='si0401_print'),
    path('vii0101/', login_required(VII0101View.as_view()), name='vii0101'),
    path('vii0101/list/', ListVII0101.as_view(), name='vii0101_list'),
    path('vii0101/filterDist/', views.DistrictVII0101View.as_view(), name='filter_dist'),
    path('vii0101/print/', PrintVII0101.as_view(), name='vii0101_print'),
    path('vi0101/', login_required(VI0101View.as_view()), name='vi0101'),
    path('vi0101/list/', ListVI0101.as_view(), name='vi0101_list'),
    path('vi0101/filterDist/', views.DistrictVI0101View.as_view(), name='filter_dist'),
    path('vi0101/print/', PrintVI0101.as_view(), name='vi0101_print'),
    path('vi0102/', login_required(VI0102View.as_view()), name='vi0102'),
    path('vi0102/list/', ListVI0102.as_view(), name='vi0102_list'),
    path('vi0102/filterDist/', views.DistrictVI0102View.as_view(), name='filter_dist'),
    path('vi0102/print/', PrintVI0102.as_view(), name='vi0102_print'),
]