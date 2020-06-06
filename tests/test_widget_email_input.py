from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class EmailWidgetTestForm(forms.Form):
    address = forms.EmailField(label="Address")


class EmailWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of email widget."""

    form_class = EmailWidgetTestForm
    tests = [
        {
            "field": "address",
            "html": (
                '<div class="form-group">'
                '<label for="id_address">Address</label>'
                '<input class="form-control" id="id_address" name="address" required type="email">'
                "</div>"
            ),
        },
        {
            "field": "address",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_address">Address</label>'
                '<input class="form-control" id="id_address" name="address" required type="email">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "address",
            "value": "alphabet",
            "html": (
                '<div class="form-group">'
                '<label for="id_address">Address</label>'
                '<input class="form-control" id="id_address" name="address" required type="email"'
                ' value="alphabet">'
                '<small class="form-text text-danger">Enter a valid email address.</small>'
                "</div>"
            ),
        },
        {
            "field": "address",
            "value": "name@example.com",
            "html": (
                '<div class="form-group">'
                '<label for="id_address">Address</label>'
                '<input class="form-control" id="id_address" name="address" required type="email"'
                ' value="name@example.com">'
                "</div>"
            ),
        },
    ]
