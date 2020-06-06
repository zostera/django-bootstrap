from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class NumberWidgetTestForm(forms.Form):
    age = forms.IntegerField(label="Age")


class NumberWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of number widget."""

    tests = [
        {
            "field": "age",
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number" maxlength="10">'
                "</div>"
            ),
        },
        {
            "field": "age",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number" maxlength="10">'
                '<small class="form-number number-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "age",
            "value": "this is more than 10 characters",
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number" maxlength="10"'
                ' value="this is more than 10 characters">'
                '<small class="form-number number-danger">Ensure this value has at most 10 characters (it has 31).</small>'
                "</div>"
            ),
        },
        {
            "field": "age",
            "value": "four",
            "html": (
                '<div class="form-group">'
                '<label for="id_age">Age</label>'
                '<input class="form-control" id="id_age" name="age" required type="number" maxlength="10"'
                ' value="four">'
                "</div>"
            ),
        },
    ]
