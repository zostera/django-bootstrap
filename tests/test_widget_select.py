from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class SelectWidgetTestForm(forms.Form):
    gender = forms.ChoiceField(
        label="Gender", choices=(("F", "she/her"), ("M", "he/him"), ("X", "they/their")), widget=forms.Select
    )


class SelectWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of gender widget."""

    form_class = SelectWidgetTestForm
    tests = [
        {
            "field": "gender",
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<select class="form-control" id="id_gender" name="gender">'
                '<option value="F">she/her</option>'
                '<option value="M">he/him</option>'
                '<option value="X">they/their</option>'
                "</select>"
                "</div>"
            ),
        },
        {
            "field": "gender",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<select class="form-control" id="id_gender" name="gender">'
                '<option value="F">she/her</option>'
                '<option value="M">he/him</option>'
                '<option value="X">they/their</option>'
                "</select>"
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "gender",
            "value": "A",
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<select class="form-control" id="id_gender" name="gender">'
                '<option value="F">she/her</option>'
                '<option value="M">he/him</option>'
                '<option value="X">they/their</option>'
                "</select>"
                '<small class="form-text text-danger">Select a valid choice. A is not one of the available choices.</small>'
                "</div>"
            ),
        },
        {
            "field": "gender",
            "value": "X",
            "html": (
                '<div class="form-group">'
                '<label for="id_gender">Gender</label>'
                '<select class="form-control" id="id_gender" name="gender">'
                '<option value="F">she/her</option>'
                '<option value="M">he/him</option>'
                '<option selected value="X">they/their</option>'
                "</select>"
                "</div>"
            ),
        },
    ]
