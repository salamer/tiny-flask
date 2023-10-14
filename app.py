from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello")
    l = []
    base = bytearray(
        1024 * 1024 * 512
    )
    print(sys.getsizeof(base))
    return "<p>Hello, Aljun!</p> {}".format(sys.getsizeof(base))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=False)