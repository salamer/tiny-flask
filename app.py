from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello")
    return "<p>Hello, Aljun!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=False)