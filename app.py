from flask import Flask, make_response
import sys

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("hello")
    # l = []
    # x = bytearray(1024*1024*1000)

    # base = bytearray(
    #     1024 * 1024 * 512
    # )
    # print(sys.getsizeof(base))
    # return "<p>Hello, Aljun!</p> {}".format(sys.getsizeof(base))
    return "<p>Hello, Aljun!</p>"


@app.route("/cookie")
def cookie():
    resp = make_response({"result": "ok"})
    resp.set_cookie(
        key="hello",
        value="world",
        httponly=True,
        domain="https://leapcell.dev"
    )
    return resp

@app.route("/cookie2")
def cookie2():
    resp = make_response({"result": "ok"})
    resp.set_cookie(
        key="hello",
        value="world",
    )
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=False)
