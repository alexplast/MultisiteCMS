from flask import Flask, send_from_directory, abort, request, redirect
from flask_sslify import SSLify
from os import path

websites = "websites"
app = Flask(__name__, static_folder=websites)
sslify = SSLify(app)


@app.get('/', defaults={'url': 'index.html'})
@app.get('/<path:url>')
def page(url):
    domain = request.headers['Host'].split(":")[0]
    files = {
        f"{websites}/{domain}/{url}": url,
        f"{websites}/{domain}/{url}index.html": "index.html",
    }
    for location, file in files.items():
        if path.isfile(location):
            return send_from_directory(f"{websites}/{domain}/", file)
        if path.isdir(location) and file[-1] != "/":
            return redirect(f"/{url}/", 301)
    return abort(404, description=domain)


@app.errorhandler(404)
def page_not_found(e):
    if path.isfile(f"{websites}/{e.description}/404.html"):
        return send_from_directory(f"{websites}/{e.description}", "404.html"), 404
    return "add 404.html", 404
