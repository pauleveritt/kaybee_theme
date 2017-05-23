"""
Implement a Page content type that can render itself
"""
from markupsafe import Markup

from kaybee_theme import Sphinx, Site
from kaybee_theme.rms import CMS


class Page:
    """ The current file that is being rendered. """
    resource_type = 'Page'

    def __init__(self, cms, resource: dict, body: str):
        # The resource is the YAML data, the body is what Sphinx
        # renders into HTML
        self.cms = cms
        self.resource = resource
        self.body = body

    def active(self, nav_id):
        """ Determine if current resource is in a given sitenav section """
        section = self.resource.get('section')
        return 'active' if section == nav_id else ''

    def __call__(self):
        template = self.cms.env.get_template('page.html')
        sphinx = Sphinx()
        site = Site()
        return template.render(page=self, sphinx=sphinx, site=Site)


@CMS.render.register(resource_type='Page')
def render_page(cms, body, resource=Page):
    page1 = Page(cms, resource,
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
    body = Markup('<p>This is the body</p>')
    this_page = cms.render(
        body,
        rpage1
    )
    print(this_page())
