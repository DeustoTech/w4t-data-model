from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from waste_collection_model.models.kpi import KPI


# Create your views here.


class KPIEditingForm(forms.ModelForm):
    class Meta:
        model = KPI
        exclude = ['orion_type', 'orion_data', 'service_path', 'updated', 'expiration', 'status', 'error']


class KPIListView(ListView):
    model = KPI


class KPIDetailView(DetailView):
    model = KPI


class CreateKpiView(CreateView):
    model = KPI
    form_class = KPIEditingForm

    success_url = reverse_lazy('kpi_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Check if everything had gone OK with orion
        if self.object.status == KPI.STATUS_OK:
            return response
        else:
            # Clean the mess and return a error response
            form.add_error(None, self.object.error)
            self.object.delete()
            return self.form_invalid(form)


class ListKpiView(ListView):
    model = KPI


class FetchKPIView(CreateView):
    model = KPI
    fields = ["orion_id"]

    success_url = reverse_lazy('kpi_list')

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # TODO load a list of of orion entities without monitored entities

    def form_valid(self, form):
        response = super().form_valid(form)
        # Check if everything had gone OK with orion
        if self.object.status == KPI.STATUS_OK:
            return response
        else:
            # Clean the mess and return a error response
            form.add_error(None, self.object.error)
            self.object.delete()
            return self.form_invalid(form)






