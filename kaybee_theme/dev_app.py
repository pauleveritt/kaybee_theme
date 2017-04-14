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

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='./static',
    template_folder='./templates'
)
app.debug = True


def pathto(fn, flag):
    """ Simulate sphinx's pathto function """
    newfn = fn[1:]  # _static -> static
    print('newfn', newfn)
    return newfn


@app.route("/")
def index():
    return render_template(
        'layout.jinja2',
        pathto=pathto
    )


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
