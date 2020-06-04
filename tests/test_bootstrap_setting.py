from django.test import TestCase, override_settings

from django_bootstrap.settings import bootstrap_setting


class BootstrapSettingTestCase(TestCase):
    """Test getting settings and overriding delaukts.."""

    def test_bootstrap_setting(self):
        self.assertEqual(bootstrap_setting("template_dir"), "django_bootstrap/bootstrap4/")

    @override_settings(DJANGO_BOOTSTRAP={"template_dir": "somewhere/else/"})
    def test_bootstrap_setting_override(self):
        self.assertEqual(bootstrap_setting("template_dir"), "somewhere/else/")
