## Flask Application for Learning Docker

from flask import Flask
import os


app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Hello World, I am running in a Docker Container."


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

