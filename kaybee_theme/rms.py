"""
Implement a Page content type that can render itself
"""
import reg
from jinja2 import Environment, PackageLoader, select_autoescape


class CMS:
    is_sphinx = False

    nav_menu = [
        dict(title='Home', url=''),
        dict(title='Blog', url='blog')
    ]

    def __init__(self, title):
        self.title = title
        self.env = Environment(
            loader=PackageLoader('kaybee_theme', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    @reg.dispatch_method(
        reg.match_key(
            'resource_type',
            lambda self, body, resource: resource.get('resource_type'))
    )
    def render(self, body, resource):
        raise NotImplementedError

    def pathto(self, fn, flag):
        """ Simulate sphinx's pathto function """

        if self.is_sphinx:
            newfn = fn  ##[1:]  # _static -> ståatic
        else:
            newfn = fn[1:]  # _static -> static
        return newfn
