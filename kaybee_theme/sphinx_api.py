"""
Mediate the API between Sphinx and the templating.

Sphinx's templating API is messy, with tons of historical layers and 
indirections. Let's put everything in one place. Then, templates know 
exactly what they are getting. Also, we can easily mock (for tests, 
for development, etc.)

These objects are intended to be injected in a Sphinx html_page_context 
hook.
"""


class Page:
    """ The current file that is being rendered. """
    title = 'Some Page'
    titlesuffix = 'Some Suffix'

    def __init__(self):
        pass

class Site:
    """ Global data and config """

    def __init__(self):
        pass