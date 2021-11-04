from django.forms.utils import flatatt
from django.utils.html import format_html

from .text import text_value


def render_script_tag(url, **kwargs):
    """Build a script tag."""
    attrs = {"src": url}
    attrs.update(kwargs)
    return render_tag("script", attrs, close=True)


def render_link_tag(url, **kwargs):
    """Build a link tag."""
    attrs = {"href": url}
    attrs.update(kwargs)
    return render_tag("link", attrs=attrs, close=False)


def render_tag(tag, attrs=None, content=None, close=True):
    """Render an HTML tag."""
    attrs_string = flatatt(attrs) if attrs else ""
    close_string = "</{tag}>" if content or close else ""
    format_string = "<{tag}" + attrs_string + ">{content}" + close_string
    return format_html(format_string, tag=tag, content=text_value(content))
