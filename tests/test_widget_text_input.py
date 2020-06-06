from django import forms

from tests.test_bootstrap_field import BootstrapFieldTestCase


class TextWidgetTestForm(forms.Form):
    content = forms.CharField(label="Content", max_length=10)


class TextWidgetTestCase(BootstrapFieldTestCase):
    """Test HTML generation of text widget."""

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
