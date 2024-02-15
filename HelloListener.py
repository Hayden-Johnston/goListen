from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/golisten", methods=['POST'])
def golisten():
    selected_mood = request.form["Mood"]
    # TODO: request song from microservice, pass song as parameter in render_template
    # microservice_URL = ''
    # song = requests.get(microservice_URL)
    return render_template("golisten.html", mood=selected_mood)

if __name__ == "__main__":
    app.run
