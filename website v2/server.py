from flask import Flask
import random

facts_list = [
    "привет",
    "4",
    "тибет"  ]

app = Flask(__name__)

@app.route("/fact")
def fact():
    var = random.choice(facts_list)
    print(var)
    return f'<p>{var}</p>'

@app.route("/")
def main_page():
    return '<a href = "/fact"> Посмотреть случайный факт</a>'

@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!</h1>"

app.run(debug=True)