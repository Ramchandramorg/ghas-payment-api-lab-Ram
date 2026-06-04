import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    result = os.popen(f"ping -c 1 {ip}").read()
    return result

app.run()