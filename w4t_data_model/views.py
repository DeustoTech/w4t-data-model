from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from w4t_waste_collection.models.monitoring import KeyPerformanceIndicator


class KPIEditingForm(forms.ModelForm):
    class Meta:
        model = KeyPerformanceIndicator
        exclude = ['orion_type', 'orion_data', 'service_path', 'updated', 'expiration', 'status', 'error']


class KPIListView(ListView):
    model = KeyPerformanceIndicator


class KPIDetailView(DetailView):
    model = KeyPerformanceIndicator


class CreateKpiView(CreateView):
    model = KeyPerformanceIndicator
    form_class = KPIEditingForm

    success_url = reverse_lazy('kpi_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Check if everything had gone OK with orion
        if self.object.status == KeyPerformanceIndicator.STATUS_OK:
            return response
        else:
            # Clean the mess and return a error response
            form.add_error(None, self.object.error)
            self.object.delete()
            return self.form_invalid(form)


class ListKpiView(ListView):
    model = KeyPerformanceIndicator


class FetchKPIView(CreateView):
    model = KeyPerformanceIndicator
    fields = ["orion_id"]

    success_url = reverse_lazy('kpi_list')

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        # TODO load a list of of orion entities without monitored entities

    def form_valid(self, form):
        response = super().form_valid(form)
        # Check if everything had gone OK with orion
        if self.object.status == KeyPerformanceIndicator.STATUS_OK:
            return response
        else:
            # Clean the mess and return a error response
            form.add_error(None, self.object.error)
            self.object.delete()
            return self.form_invalid(form)
