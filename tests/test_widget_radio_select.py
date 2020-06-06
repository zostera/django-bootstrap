from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class RadioSelectWidgetTestForm(forms.Form):
    drink = forms.ChoiceField(
        label="Drink",
        choices=(("water", "water"), ("juice", "juice",), ("tea", "tea")),
        widget=forms.RadioSelect,
    )


class RadioSelectWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of RadioSelect widget."""
    maxDiff = None
    form_class = RadioSelectWidgetTestForm
    tests = [
        {
            "field": "drink",
            "html": (
                '<div class="form-group">'
                '<label for="id_drink_0">Drink</label>'
                '<div class="form-check">'
                '<input type="radio" name="drink" class="form-check-input" value="water" id="id_drink_0">'
                '<label class="form-check-label" for="id_drink_0">water</label>'
                '</div>'
                '<div class="form-check">'
                '<input type="radio" name="drink" class="form-check-input" value="juice" id="id_drink_1">'
                '<label class="form-check-label" for="id_drink_1">juice</label>'
                '</div>'
                '<div class="form-check">'
                '<input type="radio" name="drink" class="form-check-input" value="tea" id="id_drink_2">'
                '<label class="form-check-label" for="id_drink_2">tea</label>'
                '</div>'
                '</div>'
            ),
        },
        # {
        #     "field": "drink",
        #     "data": {},
        #     "html": (
        #         '<div class="form-group">'
        #         '<label for="id_drink">Drink</label>'
        #         '<select class="form-control" id="id_drink" name="drink">'
        #         '<option value="F">she/her</option>'
        #         '<option value="M">he/him</option>'
        #         '<option value="X">they/their</option>'
        #         "</select>"
        #         '<small class="form-text text-danger">This field is required.</small>'
        #         "</div>"
        #     ),
        # },
        # {
        #     "field": "drink",
        #     "value": "A",
        #     "html": (
        #         '<div class="form-group">'
        #         '<label for="id_drink">Drink</label>'
        #         '<select class="form-control" id="id_drink" name="drink">'
        #         '<option value="F">she/her</option>'
        #         '<option value="M">he/him</option>'
        #         '<option value="X">they/their</option>'
        #         "</select>"
        #         '<small class="form-text text-danger">Select a valid choice. A is not one of the available choices.</small>'
        #         "</div>"
        #     ),
        # },
        # {
        #     "field": "drink",
        #     "value": "X",
        #     "html": (
        #         '<div class="form-group">'
        #         '<label for="id_drink">Drink</label>'
        #         '<select class="form-control" id="id_drink" name="drink">'
        #         '<option value="F">she/her</option>'
        #         '<option value="M">he/him</option>'
        #         '<option selected value="X">they/their</option>'
        #         "</select>"
        #         "</div>"
        #     ),
        # },
    ]
