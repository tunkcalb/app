from flask import Flask, render_template, request, redirect, url_for
import sys
wsgi = Flask(__name__)


@wsgi.route("/")
def hello():
    return render_template("hello.html")

@wsgi.route("/apply")
def apply():
    return render_template("apply.html")

@wsgi.route("/applyphoto")
def apply_photo():
    
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    print(location, cleaness, built_in)
    return render_template("apply_photo.html")

@wsgi.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(1))

    return redirect(url_for("hello"))

@wsgi.route("/list")
def list():
    return render_template("list.html")

    