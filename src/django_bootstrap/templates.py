from django.template.loader import get_template

from .css import merge_css_classes
from .settings import bootstrap_setting


class BootstrapTemplate:
    """Render content."""

    DEFAULT_TEMPLATE_FILE = None

    def __init__(self, *, template_file=None, template_dir=None, **kwargs):
        self.template_dir = template_dir or bootstrap_setting("template_dir", None)
        self.template_file = template_file or self.DEFAULT_TEMPLATE_FILE
        self.kwargs = kwargs

    def get_template_dir(self):
        return self.template_dir

    def get_template_file(self):
        return self.template_file

    def get_template_name(self):
        """Return template name for file."""
        template_dir = self.get_template_dir()
        template_file = self.get_template_file()
        assert template_dir, "Template directory is not set."
        assert template_file, "Template file is not set."
        return f"{self.template_dir}{self.template_file}"

    def get_context(self):
        """Return context for template."""
        return {}

    def get_template(self, template_name=None):
        """Return the template to render."""
        return get_template(template_name or self.get_template_name())

    def render(self):
        """Return rendered content using template and context."""
        template = self.get_template()
        context = self.get_context()
        return template.render(context)


class BootstrapFormSetTemplate(BootstrapTemplate):
    """Render form set."""

    DEFAULT_TEMPLATE_FILE = "forms/form_set.html"

    def __init__(self, form_set, **kwargs):
        self.form_set = form_set
        super().__init__(**kwargs)

    def get_context(self):
        context = super().get_context()
        context["form_set"] = self.form_set
        return context


class BootstrapFormTemplate(BootstrapTemplate):
    """Render form."""

    DEFAULT_TEMPLATE_FILE = "forms/form.html"

    def __init__(self, form, **kwargs):
        self.form = form
        super().__init__(**kwargs)

    def get_context(self):
        context = super().get_context()
        context["form"] = self.form
        return context


class BootstrapFieldTemplate(BootstrapTemplate):
    """Render field."""

    DEFAULT_TEMPLATE_FILE = "forms/field.html"

    def __init__(self, field, **kwargs):
        self.field = field
        super().__init__(**kwargs)

    def get_widget_context(self, only_initial=False):
        """Return widget context."""
        field = self.field
        widget = field.field.hidden_widget() if only_initial else field.field.widget
        if field.field.localize:
            widget.is_localized = True

        # Build attributes for widget
        attrs = field.build_widget_attrs(field.field.widget_attrs(widget), widget)
        if field.auto_id and "id" not in widget.attrs:
            attrs.setdefault("id", field.html_initial_id if only_initial else field.auto_id)
        widget_context = widget.get_context(
            name=field.html_initial_name if only_initial else field.html_name, value=field.value(), attrs=attrs
        ).get("widget", {})

        # TODO: There must be a better way to do this
        optgroups = widget_context.get("optgroups")
        if optgroups:
            patched_optgroups = []
            for optgroup in optgroups:
                name = optgroup[0]
                options = optgroup[1]
                index = optgroup[2]
                patched_options = []
                for option in options:
                    template_name = option.get("template_name", "")
                    option["bootstrap_template_name"] = template_name.replace("django/", self.get_template_dir(), 1)
                    patched_options.append(option)
                patched_optgroups.append((name, options, index))
            widget_context["optgroups"] = patched_optgroups

        widget_context["attrs"]["class"] = merge_css_classes(
            widget_context["attrs"].get("class", ""), self.kwargs.get("extra_classes", ""), "form-control"
        )

        template_name = widget_context.get("template_name", "")
        widget_context["bootstrap_template_name"] = template_name.replace("django/", self.get_template_dir(), 1)

        return widget_context

    def get_context(self, only_initial=False):
        context = super().get_context()
        context["field"] = self.field
        context["widget"] = self.get_widget_context(only_initial)
        context["kwargs"] = self.kwargs
        context["show_label"] = self.kwargs.get("show_label", True)
        context["form_group_class"] = self.kwargs.get("form_group_class", "form-group")
        context["addon_before"] = self.kwargs.get("addon_before", "")
        context["addon_after"] = self.kwargs.get("addon_before", "")
        return context

    def render(self):
        output = super().render()
        if self.field.field.show_hidden_initial:
            context = self.get_context(only_initial=True)
            template = get_template()
            output += template.render(context)
        return output
