SECRET_KEY = "Thanks for using django-bootstrap!"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = (
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    # Our tests
    "django_bootstrap",
    "tests",
)

ROOT_URLCONF = "tests.app.urls"

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # required for django.contrib.admin
    "django.contrib.messages.middleware.MessageMiddleware",  # required for django.contrib.admin
)

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

BOOTSTRAP4 = {
    "theme_url": "//example.com/theme.css",
    "javascript_in_head": True,
    "required_css_class": "django_bootstrap-req",
    "error_css_class": "django_bootstrap-err",
    "success_css_class": "django_bootstrap-bound",
}
