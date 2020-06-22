from bs4 import BeautifulSoup
from django import forms
from django.test import TestCase

from tests.compat import django3_html
from tests.test_template_tags import render_template


class XssTestForm(forms.Form):
    danger = forms.CharField(label='XSS" onmouseover="alert(\'Hello, XSS\')" foo="', max_length=100)


class XssTestCase(TestCase):
    """Test handling of XSS vulnerabilities."""

    # def test_xss_field(self):
    #     form = XssTestForm()
    #     output = render_template("{% bootstrap_field form.danger %}", form=form)
    #     soup = BeautifulSoup(output, 'html.parser')
    #
    #
    #
    #     self.assertIn('type="text"', output)
    #
    #     self.assertIn(
    #         django3_html(
    #             '<label for="id_danger">'
    #             "XSS&quot; onmouseover=&quot;alert(&#x27;Hello, XSS&#x27;)&quot; foo=&quot;</label>"
    #         ),
    #         output,
    #     )
    #     self.assertIn(
    #         django3_html('placeholder="XSS&quot; onmouseover=&quot;alert(&#x27;Hello, XSS&#x27;)&quot; foo=&quot;"'),
    #         output,
    #     )
