"""
This example shows how to graft a WSGI app onto mitmproxy. In this
instance, we're using the Flask framework (http://flask.pocoo.org/) to expose
a single simplest-possible page.
"""
from flask import Flask
from mitmproxy.addons import wsgiapp

app = Flask("proxapp")


@app.route('/')
def hello_world():
    return 'Hello World!'


def start(opts):
    # Host app at the magic domain "proxapp" on port 80. Requests to this
    # domain and port combination will now be routed to the WSGI app instance.
    return wsgiapp.WSGIApp(app, "proxapp", 80)

    # SSL works too, but the magic domain needs to be resolvable from the mitmproxy machine due to mitmproxy's design.
    # mitmproxy will connect to said domain and use serve its certificate (unless --no-upstream-cert is set)
    # but won't send any data.
    # mitmproxy.ctx.master.apps.add(app, "example.com", 443)
