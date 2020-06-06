from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class NumberWidgetTestForm(forms.Form):
    age = forms.IntegerField(label="Age")


class NumberWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of number widget."""
    form_class = NumberWidgetTestForm
    tests = [
        {
            "field": "age",
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number">'
                "</div>"
            ),
        },
        {
            "field": "age",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "age",
            "value": "alphabet",
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number"'
                ' value="alphabet">'
                '<small class="form-text text-danger">Enter a whole number.</small>'
                "</div>"
            ),
        },
        {
            "field": "age",
            "value": "4",
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number"'
                ' value="4">'
                "</div>"
            ),
        },
    ]
