from django.forms import EmailInput, NumberInput, PasswordInput, Textarea, TextInput, URLInput

WIDGETS_WITH_PLACEHOLDERS = (TextInput, Textarea, NumberInput, EmailInput, URLInput, PasswordInput)


def is_widget_with_placeholder(widget):
    """
    Return whether this widget should have a placeholder.

    Only text, text area, number, e-mail, url, password, number and derived inputs have placeholders.
    """
    return isinstance(widget, WIDGETS_WITH_PLACEHOLDERS)
