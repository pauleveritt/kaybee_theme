"""
Implement a Page content type that can render itself
"""
import reg
from markupsafe import Markup
from jinja2 import Environment, PackageLoader, select_autoescape

from kaybee_theme import Sphinx, Site


class CMS:
    def __init__(self, title):
        self.title = title

    @reg.dispatch_method(
        reg.match_key(
            'resource_type',
            lambda self, resource: resource.get('resource_type'))
    )
    def render(self, resource):
        raise NotImplementedError


env = Environment(
    loader=PackageLoader('kaybee_theme', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


class Page:
    """ The current file that is being rendered. """
    resource_type = 'Page'

    def __init__(self, resource: dict, body: str):
        # The resource is the YAML data, the body is what Sphinx
        # renders into HTML
        self.resource = resource
        self.body = body

    def active(self, nav_id):
        """ Determine if current resource is in a given sitenav section """
        section = self.resource.get('section')
        return 'active' if section == nav_id else ''

    def __call__(self):
        template = env.get_template('page.html')
        sphinx = Sphinx()
        site = Site()
        return template.render(page=self, sphinx=sphinx, site=Site)


@CMS.render.register(resource_type='Page')
def render_page(cms, resource):
    page1 = Page(resource,
                 body=Markup('<p>This is the body</p>')
                 )
    return page1


if __name__ == '__main__':
    rpage1 = dict(
        title='Resource Page 1',
        subtitle='RP1 is subtitled',
        resource_type='Page',
        section='Home'
    )
    cms = CMS('Some Sphinx docs site')
    this_page = cms.render(rpage1)
    print(this_page())
