"""
Fake the Kaybee/Sphinx API.

Sphinx's templating API is messy, with tons of historical layers and 
indirections. Kaybee flattens all of that, along with its own features, 
into one place.

When writing a theme, we don't want the real Kaybee API, as we don't 
want Sphinx etc. until we have to. So let's make a fake instance of 
the Kaybee API.
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


class Sphinx:
    """ Utilities etc. from sphinx """

    def __init__(self, is_flask: bool = True):
        self.is_flask = is_flask

    def pathto(self, fn, flag):
        """ Simulate sphinx's pathto function """

        if self.is_flask:
            newfn = fn[1:]  # _static -> static
        else:
            newfn = fn  ##[1:]  # _static -> ståatic
        return newfn
