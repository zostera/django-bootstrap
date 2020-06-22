def django3_html(html):
    """
    Return HTML string with &#x27; (Django >= 3) instead of &#39; (Django < 3).

    See https://docs.djangoproject.com/en/dev/releases/3.0/#miscellaneous
    """
    return html.replace("&#39;", "&#x27;")
