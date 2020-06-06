from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class UrlWidgetTestForm(forms.Form):
    website = forms.UrlField(label="Website")


class UrlWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of url widget."""
    form_class = UrlWidgetTestForm
    tests = [
        {
            "field": "website",
            "html": (
                '<div class="form-group">'
                '<label for="id_website">Website</label>'
                '<input class="form-control" id="id_website" name="website" required type="url">'
                "</div>"
            ),
        },
        {
            "field": "website",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_website">Website</label>'
                '<input class="form-control" id="id_website" name="website" required type="url">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "website",
            "value": "alphabet",
            "html": (
                '<div class="form-group">'
                '<label for="id_website">Website</label>'
                '<input class="form-control" id="id_website" name="website" required type="url"'
                ' value="alphabet">'
                '<small class="form-text text-danger">Enter a valid url website.</small>'
                "</div>"
            ),
        },
        {
            "field": "website",
            "value": "name@example.com",
            "html": (
                '<div class="form-group">'
                '<label for="id_website">Website</label>'
                '<input class="form-control" id="id_website" name="website" required type="url"'
                ' value="name@example.com">'
                "</div>"
            ),
        },
    ]
