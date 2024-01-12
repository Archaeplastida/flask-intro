from flask import Flask
app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/<location>")
def welcome_location(location= ""):
    return f"welcome {location}"