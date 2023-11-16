from flask import Flask, make_response, request
import sys
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    # print("hello")
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
        domain="https://leapcell.dev",
        expires=datetime.date.today() + datetime.timedelta(days=7)
    )
    resp.set_cookie(
        key="qqq",
        value="wwww",
        httponly=True,
        domain="https://leapcell.dev",
        expires=datetime.date.today() + datetime.timedelta(days=7)
    )
    return resp


@app.route("/cookie3")
def cookie3():
    resp = make_response({"result": "ok"})
    resp.set_cookie(
        key="hello",
        value="world",
        httponly=True,
        domain=".leapcell.dev",
        expires=datetime.date.today() + datetime.timedelta(days=7)
    )
    resp.set_cookie(
        key="qqq",
        value="wwww",
        httponly=True,
        domain=".leapcell.dev",
        expires=datetime.date.today() + datetime.timedelta(days=7)
    )
    return resp


@app.route("/cookie2")
def cookie2():
    resp = make_response({"result": "ok"})
    resp.set_cookie(
        key="hello",
        value="world",
        expires=datetime.date.today() + datetime.timedelta(days=7)
    )
    resp.set_cookie(
        key="hi",
        value="aljun",
        expires=datetime.date.today() + datetime.timedelta(days=7)
    )
    return resp

@app.route("/headers")
def headers():
    print(request.headers)
    return {"headers": dict(request.headers)}

@app.route("/multi_string")
def multi_string():
    return "Multi\nLine\nResponse" * 1000

@app.route("/multi_json")
def multi_json():
    res = {}
    for i in range(1000):
        res[i] = i
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=False)
