from django import forms
from django.test import TestCase

from tests.test_template_tags import render_template


class InputFieldTestForm(forms.Form):
    content = forms.CharField(label="Content", max_length=10)


class BootstrapFieldTestCase(TestCase):
    """Test bootstrap field HTML output."""

    maxDiff = None

    form_class = None
    tests = []

    def test_tests(self):
        if self.form_class:
            form_class = self.form_class
            for test in self.tests:
                field = test["field"]
                html = test["html"]
                data = test.get("data", None)
                if "value" in test:
                    data = data or {}
                    data[field] = test["value"]
                if data is None:
                    form = form_class()
                else:
                    form = form_class(data=data)
                    form.is_valid()
                output = render_template("{% bootstrap_field form." + field + " %}", form=form)
                self.assertHTMLEqual(output, html)


class InputFieldTestCase(BootstrapFieldTestCase):
    """Test input field."""

    form_class = InputFieldTestForm
    tests = [
        {
            "field": "content",
            "html": (
                '<div class="form-group">'
                '<label for="id_content">Content</label>'
                '<input class="form-control" id="id_content" name="content" required type="text" maxlength="10">'
                "</div>"
            ),
        },
        {
            "field": "content",
            "data": {},
            "html": (
                '<div class="form-group">'
                '<label for="id_content">Content</label>'
                '<input class="form-control" id="id_content" name="content" required type="text" maxlength="10">'
                '<small class="form-text text-danger">This field is required.</small>'
                "</div>"
            ),
        },
        {
            "field": "content",
            "value": "this is more than 10 characters",
            "html": (
                '<div class="form-group">'
                '<label for="id_content">Content</label>'
                '<input class="form-control" id="id_content" name="content" required type="text" maxlength="10"'
                ' value="this is more than 10 characters">'
                '<small class="form-text text-danger">Ensure this value has at most 10 characters (it has 31).</small>'
                "</div>"
            ),
        },
        {
            "field": "content",
            "value": "four",
            "html": (
                '<div class="form-group">'
                '<label for="id_content">Content</label>'
                '<input class="form-control" id="id_content" name="content" required type="text" maxlength="10"'
                ' value="four">'
                "</div>"
            ),
        },
    ]
