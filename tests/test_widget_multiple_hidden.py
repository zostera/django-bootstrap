from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class GenderWidgetTestForm(forms.Form):
    gender = forms.ChoiceField(label="Gender", choices=(("F", "she/her"), ("M", "he/him"), ("X", "they/their")))



class GenderWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of gender widget."""
    form_class = GenderWidgetTestForm
    tests = [
        {
            "field": "gender",
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<input class="form-control" id="id_gender" name="gender" required type="gender">'
                "</div>"
            ),
        },
        {
            "field": "gender",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<input class="form-control" id="id_gender" name="gender" required type="gender">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "gender",
            "value": "alphabet",
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<input class="form-control" id="id_gender" name="gender" required type="gender"'
                ' value="alphabet">'
                '<small class="form-text text-danger">Enter a valid gender gender.</small>'
                "</div>"
            ),
        },
        {
            "field": "gender",
            "value": "name@example.com",
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<input class="form-control" id="id_gender" name="gender" required type="gender"'
                ' value="name@example.com">'
                "</div>"
            ),
        },
    ]
