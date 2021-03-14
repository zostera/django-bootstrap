def _css_class_list(value):
    """Return list without duplicate or empty elements."""
    return filter(None, list(dict.fromkeys(value)))


def _css_class_list_string(value):
    """Return list without duplicate or empty elements."""
    return " ".join(_css_class_list(value))


def merge_css_classes(*args, prepend=False):
    """Merge CSS classes into one string."""
    if prepend:
        args = list(reversed(args))
    css_classes = []
    for arg in args:
        css_classes += f"{arg}".split(" ")
    return _css_class_list_string(css_classes)
