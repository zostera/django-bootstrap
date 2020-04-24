def merge_css_classes(*args):
    """Merge CSS classes into one string."""
    css_classes = []
    for arg in args:
        css_classes += f"{arg}".split(" ") if arg else []
    return " ".join(list(set(css_classes)))
