from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class HiddenWidgetTestForm(forms.Form):
    secret = forms.CharField(widget=forms.HiddenInput)


class HiddenWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of hidden widget."""

    form_class = HiddenWidgetTestForm
    tests = [
        {"field": "secret", "html": ('<input class="form-control" id="id_secret" name="secret" type="hidden">'),},
        {
            "field": "secret",
            "data": {},
            "html": ('<input class="form-control" id="id_secret" name="secret" type="hidden">'),
        },
        {
            "field": "secret",
            "value": "alphabet",
            "html": ('<input class="form-control" id="id_secret" name="secret" type="hidden"' ' value="alphabet">'),
        },
    ]
