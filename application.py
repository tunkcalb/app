from flask import Flask, render_template, request, redirect
import sys
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/apply")
def apply():
    return render_template("apply.html")

@application.route("/applyphoto")
def apply_photo():
    
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    print(location, cleaness, built_in)
    return render_template("apply_photo.html")

@application.route("/upload_done", methods=["POST"])
def upload_done():
    upladed_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(1))

    return redirect(url_for("hello"))

@application.route("/list")
def list():
    return render_template("list.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')
    