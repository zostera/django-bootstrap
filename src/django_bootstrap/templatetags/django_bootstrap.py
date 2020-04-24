from django import template

from ..templates import BootstrapFieldTemplate, BootstrapFormSetTemplate, BootstrapFormTemplate

register = template.Library()


@register.simple_tag
def bootstrap_form_set(form_set, **kwargs):
    """Render a form set."""
    bootstrap_template = BootstrapFormSetTemplate(form_set, **kwargs)
    return bootstrap_template.render()


@register.simple_tag
def bootstrap_form(form, **kwargs):
    """Render a form."""
    bootstrap_template = BootstrapFormTemplate(form, **kwargs)
    return bootstrap_template.render()


@register.simple_tag
def bootstrap_field(field, **kwargs):
    """Render a form field."""
    bootstrap_template = BootstrapFieldTemplate(field, **kwargs)
    return bootstrap_template.render()
