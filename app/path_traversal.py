from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/read')
def read_file():
    filename = request.args.get('file')
    with open("files/" + filename, "r") as f:
        return f.read()

app.run()
