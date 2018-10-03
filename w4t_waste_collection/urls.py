
from w4t_waste_collection.views import CreateKpiView, ListKpiView, FetchKPIView
from django.urls import path


urlpatterns = [
    path('create/', CreateKpiView.as_view(), name='kpi_create'),
    path('list/', ListKpiView.as_view(), name='kpi_list'),
    path('fetch/', FetchKPIView.as_view(), name='kpi_fetch'),
]
