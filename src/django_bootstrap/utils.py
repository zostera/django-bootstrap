import re
from collections.abc import Mapping
from urllib.parse import parse_qs, urlparse, urlunparse

from django.template.base import FilterExpression, TemplateSyntaxError, Variable, VariableDoesNotExist, kwarg_re
from django.template.loader import get_template
from django.utils.encoding import force_str
from django.utils.http import urlencode

# RegEx for quoted string
QUOTED_STRING = re.compile(r'^["\'](?P<noquotes>.+)["\']$')


def handle_var(value, context):
    """Handle template tag variable."""
    # Resolve FilterExpression and Variable immediately
    if isinstance(value, FilterExpression) or isinstance(value, Variable):
        return value.resolve(context)
    # Return quoted strings unquoted
    # http://djangosnippets.org/snippets/886
    stringval = QUOTED_STRING.search(value)
    if stringval:
        return stringval.group("noquotes")
    # Resolve variable or return string value
    try:
        return Variable(value).resolve(context)
    except VariableDoesNotExist:
        return value


def parse_token_contents(parser, token):
    """Parse template tag contents."""
    bits = token.split_contents()
    tag = bits.pop(0)
    args = []
    kwargs = {}
    asvar = None
    if len(bits) >= 2 and bits[-2] == "as":
        asvar = bits[-1]
        bits = bits[:-2]
    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError('Malformed arguments to tag "{tag}"'.format(tag=tag))
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))
    return {"tag": tag, "args": args, "kwargs": kwargs, "asvar": asvar}


def render_template_file(template, context=None):
    """Render a Template to unicode."""
    assert isinstance(context, Mapping)
    template = get_template(template)
    return template.render(context)


def url_replace_param(url, name, value):
    """Replace a GET parameter in a URL."""
    url_components = urlparse(force_str(url))

    params = parse_qs(url_components.query)

    params[name] = value
    if value is None:
        del params[name]

    return urlunparse(
        [
            url_components.scheme,
            url_components.netloc,
            url_components.path,
            url_components.params,
            urlencode(params, doseq=True),
            url_components.fragment,
        ]
    )


def get_url_attrs(url, url_attr):
    """Return dict with attrs for url."""
    if isinstance(url, str):
        return {url_attr: url}
    return url.copy()
