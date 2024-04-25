from flask import Flask
from flask import render_template, request
import pandas as pd
import ml_model.model

name = "main"
app = Flask(name)

data = pd.read_csv("C:/src/recommendation_system/BigData_project/data/Coursera.csv")


@app.route('/', methods=["POST", "GET"])
def recommend_system():
    if request.method == "GET":
        return render_template('index.html', data=data['Course Name'].to_list())
    if request.method == "POST":
        course_name = request.form.get('courseName')
        result = ml_model.model.recommend(course_name)
        return ', '.join(result)


if name == 'main':
    app.run(debug=True)
