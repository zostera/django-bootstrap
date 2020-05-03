from django.views.generic import FormView, TemplateView

from .forms import DemoForm


class HomeView(TemplateView):
    template_name = "home.html"


class TestFormView(FormView):
    form_class = DemoForm
    template_name = "form.html"
