from functools import wraps


def make_html(element):
    def decorator_make_html(func):
        @wraps(func)
        def wrapper_make_html(*args, **kwargs):
            result = func(*args, **kwargs)
            html = f"<{element}>{result}</{element}>"
            return html

        return wrapper_make_html

    return decorator_make_html


@make_html("p")
@make_html("strong")
def get_text(text="I code with PyBites"):
    return text


html1 = get_text("Monkey!")
html2 = get_text()
html3 = get_text("Banana!")
pass
