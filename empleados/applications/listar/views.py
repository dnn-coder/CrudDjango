from django.shortcuts import render
from .models import TablaEmpleado, TablaNomina
from.forms import EmpleadosForm, NominaForm

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# class ListarView(TemplateView):
#     template_name='listar.html'

class EmpleadosListView(ListView):
    template_name = "listar.html"
    model = TablaEmpleado
    context_object_name = 'listar'

class NominaListView(ListView):
    template_name = "listarn.html"
    model = TablaNomina
    context_object_name = 'listarn'

class EmpleadosCreateView(CreateView):
    model = TablaEmpleado
    context_object_name = '/creare'
    template_name = "creare.html"
    form_class = EmpleadosForm
    success_url = '/listar'

class NominaCreateView(CreateView):
    model = TablaNomina
    context_object_name = '/crearn'
    template_name = "crearn.html"
    form_class = NominaForm
    success_url = '/listarn'

class EmpleadosUpdateView(UpdateView):
    model = TablaEmpleado
    template_name = "actualizare.html"
    fields=('__all__')
    success_url = '/listar'

class NominaUpdateView(UpdateView):
    model = TablaNomina
    template_name = "actualizarn.html"
    fields=('__all__')
    success_url = '/listarn'

class EmpleadosDeleteView(DeleteView):
    model = TablaEmpleado
    template_name = "eliminare.html"
    fields=('__all__')
    success_url = '/listar'

class NominaDeleteView(DeleteView):
    model = TablaNomina
    template_name = "eliminarn.html"
    fields=('__all__')
    success_url = '/listarn'



