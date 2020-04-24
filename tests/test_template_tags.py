from django.template import Context, Template
from django.test import TestCase

TEMPLATE_BASE = "{% load django_bootstrap %}"


def render_template(content, **context_args):
    """Create a template that loads the template base and adds the given content."""
    template = Template(f"{TEMPLATE_BASE}{content}")
    return template.render(Context(context_args))


class TemplateTagsTestCase(TestCase):
    """Test template tags."""

    def test_empty_template(self):
        self.assertEqual(render_template(""), "")

    def test_non_empty_template(self):
        self.assertEqual(render_template("And so, it begins"), "And so, it begins")
