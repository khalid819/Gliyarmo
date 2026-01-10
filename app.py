from flask import Flask,render_template,jsonify
from flask_cors import CORS
from openai import OpenAI
app = Flask(__name__,static_folder="static")
CORS(app) 
OPENROUTER_API_KEY="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"
def chat():
   client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
  )

   completion = client.chat.completions.create(
    extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", 
       "X-Title": "<YOUR_SITE_NAME>", 

  },
  extra_body={},
  model="openai/gpt-oss-120b:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
   print(completion.choices[0].message.content)
chat()
   

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/doc")
def docs():
    return render_template("docs.html") 
@app.route("/tools")
def generator():
    return render_template("tool.html")
@app.route("/solver")
def solver():
    return render_template("solver.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/trans")
def trans():
    return render_template("trans.html")
@app.route("/chat")
def chat():
    return render_template("ai_chat.html")
@app.route("/question")
def question():
    return render_template("questions.html")
@app.route("/help")
def help():
    return render_template("help.html")

app.run(debug=True) 