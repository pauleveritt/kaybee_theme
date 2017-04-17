import os

from kaybee_theme.sphinx_api import Page


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def get_html_templates_path():
    """Return path to theme's template folder.

    Used by the doc project's config.py to hook into the template 
    setup.
    """

    pkgdir = os.path.abspath(os.path.dirname(__file__))
    return [os.path.join(pkgdir, 'templates')]


def update_context(app, pagename, templatename, context, doctree):
    context['theme_version'] = 0.1
    context['page'] = Page()


def setup(app):
    app.connect('html-page-context', update_context)
    return {'version': 0.1,
            'parallel_read_safe': True}
