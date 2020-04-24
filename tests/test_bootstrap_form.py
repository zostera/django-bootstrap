from django import forms
from django.test import TestCase

from .test_template_tags import render_template


class TestForm(forms.Form):
    name = forms.CharField(label="Name")


class InputFieldTestCase(TestCase):
    """Test input field."""

    def test_form(self):
        test_form = TestForm()
        self.assertHTMLEqual(
            render_template("{% bootstrap_form test_form %}", test_form=test_form),
            (
                '<div class="form-group">'
                '<label for="id_name">Name</label>'
                '<input class="form-control" id="id_name" name="name" required type="text">'
                "</div>"
            ),
        )
        test_form = TestForm(data={})
        self.assertHTMLEqual(
            render_template("{% bootstrap_form test_form %}", test_form=test_form),
            (
                '<div class="form-group">'
                '<label for="id_name">Name</label>'
                '<input class="form-control" id="id_name" name="name" required type="text">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        )
