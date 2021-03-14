from django.test import TestCase

from django_bootstrap.css import merge_css_classes


class CssTest(TestCase):
    """Test CSS functions."""

    def test_merge_css_classes(self):
        self.assertEqual("", merge_css_classes())
        self.assertEqual("", merge_css_classes(""))
        self.assertEqual("", merge_css_classes("", ""))
