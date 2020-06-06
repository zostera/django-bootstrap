from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class PasswordWidgetTestForm(forms.Form):
    secret = forms.CharField(label="Secret", widget=forms.PasswordInput, min_length=5)


class PasswordWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of password widget."""

    form_class = PasswordWidgetTestForm
    tests = [
        {
            "field": "secret",
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required minlength="5" type="password">'
                "</div>"
            ),
        },
        {
            "field": "secret",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required minlength="5" type="password">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "secret",
            "value": "four",
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required minlength="5" type="password">'
                '<small class="form-text text-danger">Ensure this value has at least 5 characters (it has 4).</small>'
                "</div>"
            ),
        },
        {
            "field": "secret",
            "value": "this.is.a.secret",
            "html": (
                '<div class="form-group">'
                '<label for="id_secret">Secret</label>'
                '<input class="form-control" id="id_secret" name="secret" required minlength="5" type="password">'
                "</div>"
            ),
        },
    ]
