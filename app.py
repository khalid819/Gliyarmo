from flask import Flask,render_template
from flask_cors import CORS
app = Flask(__name__,static_folder="static")
CORS(app) 
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/doc")
def docs():
    return render_template("docs.html") 
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.errorhandler(404)
def lost(error):
    return render_template("lost.html")
app.run(debug=True) 
