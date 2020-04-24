from django.views.generic import FormView, TemplateView

from .forms import TestForm


class HomeView(TemplateView):
    template_name = "home.html"


class TestFormView(FormView):
    form_class = TestForm
    template_name = "form.html"
