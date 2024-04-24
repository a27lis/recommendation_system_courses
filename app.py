from flask import Flask
from flask import render_template
name = "main"
app = Flask(name)

@app.route('/')
def hello_world():
  return render_template('index.html')

if name == 'main':
  app.run(debug=True)