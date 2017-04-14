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
    static_url_path='/dist',
    static_folder='dist',
    template_folder='src/templates'
)
app.debug = True


@app.route("/")
def hello():
    return render_template('layout.jinja2', name='Hello')


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()

# app is a Flask object
# app = create_app()

# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
# app.debug = True
