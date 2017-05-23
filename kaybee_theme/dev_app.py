"""
Development server for hacking kaybee_theme

This is a small Flask server which speeds up development of the 
theme. It is not bundled into the distribution. Its job is to 
replace the edit, run sphinx, reload browser cycle.

It provides:

- An instance of the context for use in the templates

- Some representative sample data

- A livereload-capable server

"""
from flask import Flask
from livereload import Server
from markupsafe import Markup

from kaybee_theme.rms import CMS
from kaybee_theme.page import Page
Page # Prevent Optimize Imports from whacking this

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='./static',
    template_folder='./templates'
)
app.debug = True


@app.route("/")
def index():
    cms = CMS('Some Sphinx docs site')
    resource1 = dict(
        title='Resource Page 1',
        subtitle='RP1 is subtitled',
        resource_type='Page',
        section='Home'
    )
    body = Markup('<p>This is the body</p>')
    this_page = cms.render(
        body,
        resource1
    )
    return this_page()


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
