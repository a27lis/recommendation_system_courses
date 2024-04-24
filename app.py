from flask import Flask
from flask import render_template, request
import pandas as pd

name = "main"
app = Flask(name)

data = pd.read_csv("C:/src/recommendation_system/BigData_project/data/Coursera.csv")
data = data[['Course Name', 'Difficulty Level', 'Course Description', 'Skills']]


@app.route('/', methods=["POST", "GET"])
def recommend_system():
    if request.method == "GET":
        return render_template('index.html', data=data['Course Name'].to_list())


if name == 'main':
    app.run(debug=True)
