from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class UrlWidgetTestForm(forms.Form):
    secret = forms.CharField(label="Secret", widget=forms.PasswordInput)


class UrlWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of url widget."""
    form_class = UrlWidgetTestForm
    tests = [
        {
            "field": "secret",
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required type="url">'
                "</div>"
            ),
        },
        {
            "field": "secret",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required type="url">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "secret",
            "value": "alphabet",
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required type="url"'
                ' value="alphabet">'
                '<small class="form-text text-danger">Enter a valid URL.</small>'
                "</div>"
            ),
        },
        {
            "field": "secret",
            "value": "https://example.com",
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required type="url"'
                ' value="https://example.com">'
                "</div>"
            ),
        },
    ]
