from flask import Flask

app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>Hello world,this is by docker and flask</h1>"