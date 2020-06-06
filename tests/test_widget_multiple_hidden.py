from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class MultipleHiddenWidgetTestForm(forms.Form):
    gender = forms.MultipleChoiceField(label="Gender", choices=(("F", "she/her"), ("M", "he/him"), ("X", "they/their")), widget=forms.MultipleHiddenInput)


class MultipleHiddenWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of gender widget."""
    form_class = MultipleHiddenWidgetTestForm
    tests = [
        {
            "field": "gender",
            "html": "",
        },
        {
            "field": "gender",
            "data": {},
            "html": "",
        },
        {
            "field": "gender",
            "value": "F",
            "html": (
                '<input class="form-control" id="id_gender" name="gender" type="hidden" value="F">'
            ),
        },
    ]
