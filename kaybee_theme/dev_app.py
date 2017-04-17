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
from flask import Flask, render_template
from livereload import Server

from kaybee_theme.fake_kaybee_api import Page, Site, Sphinx

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='./static',
    template_folder='./templates'
)
app.debug = True


@app.route("/")
def index():
    return render_template(
        'layout.html',
        page=Page(),
        site=Site(),
        sphinx=Sphinx()
    )


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
