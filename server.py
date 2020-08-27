#!/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/<pagename>")
def return_static_page(pagename):
    print(pagename)
    return app.send_static_file(pagename)

@app.route("/rb/5k/cj,nj/<name>")
def return_script(name):
    print(name)
    return app.send_static_file(name)

if __name__ == "__main__":
    app.run(host="10.0.2.15", port=5000)
