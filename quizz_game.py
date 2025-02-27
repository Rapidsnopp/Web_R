from flask import Flask, render_template, request, redirect, url_for

app = Flask("My App")
@app.route("/, methods=['GET', 'POST']")

def welcome():
    return "<h1>Welcome to the Quizz Game!</h1>"

if __name__ == "__main__":
    app.run(debug=True)