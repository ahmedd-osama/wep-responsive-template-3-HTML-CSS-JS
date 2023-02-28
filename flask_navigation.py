from flask import Flask, render_template

artlly = Flask(__name__)

@artlly.route("/")
def homepage():
  return render_template("index.html", pagetitle="Homepage")

@artlly.route("/contact")
def contact():
  return render_template("contact.html", pagetitle="Contact Us")

@artlly.route("/log_in")
def log_in():
  return render_template("log_in.html", pagetitle="log In")

@artlly.route("/join")
def join():
  return render_template("join.html", pagetitle="join", custom_css = "add")
# @artlly.route("/skills")
# def skills():
#   return render_template("skills.html", pagetitle="skills", skills = skills_list)

if __name__ == "__main__":
  artlly.run(debug=False, port=8000)