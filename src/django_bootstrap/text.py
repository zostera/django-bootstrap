from django.utils.encoding import force_str


def text_value(value):
    """Force a value to text, render None as an empty string."""
    return "" if value is None else force_str(value)


def text_concat(*args, separator=""):
    """Concatenate arguments as a text string with an optional separator."""
    separator = text_value(separator)
    return separator.join(filter(None, [text_value(arg) for arg in args]))
