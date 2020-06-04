from django.conf import settings

DJANGO_BOOTSTRAP_DEFAULTS = {"template_dir": "django_bootstrap/bootstrap4/"}


def bootstrap_setting(name, default=None):
    """Return requested bootstrap setting it exists in settings or defaults, otherwise the given default value."""
    bootstrap3_settings = getattr(settings, "DJANGO_BOOTSTRAP", {})
    return bootstrap3_settings.get(name, DJANGO_BOOTSTRAP_DEFAULTS.get(name, default))
