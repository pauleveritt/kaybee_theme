import os


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context['theme_version'] = 0.1


def setup(app):
    app.connect('html-page-context', update_context)
    return {'version': 0.1,
            'parallel_read_safe': True}
