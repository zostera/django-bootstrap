from django.conf import settings

DEFAULT_SETTINGS = {"template_dir": "django_bootstrap/bootstrap4/"}


def bootstrap_setting(name, default):
    """Return value for bootstrap setting if it exists, otherwise the given default value."""
    try:
        django_bootstrap_settings = settings.DJANGO_BOOTSTRAP
    except AttributeError:
        django_bootstrap_settings = DEFAULT_SETTINGS
    return django_bootstrap_settings.get(name, default)
