from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello")
    l = []
    base = "*" * 1024
    for i in range(0, 1024*1024):
        l.append(base)
    print("mem", sys.getsizeof(l))
    return "<p>Hello, Aljun!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=False)