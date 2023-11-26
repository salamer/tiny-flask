from flask import Flask, make_response, request
import sys
import datetime
import threading

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
        expires=datetime.date.today() + datetime.timedelta(days=7),
    )
    resp.set_cookie(
        key="qqq",
        value="wwww",
        httponly=True,
        domain="https://leapcell.dev",
        expires=datetime.date.today() + datetime.timedelta(days=7),
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
        expires=datetime.date.today() + datetime.timedelta(days=7),
    )
    resp.set_cookie(
        key="qqq",
        value="wwww",
        httponly=True,
        domain=".leapcell.dev",
        expires=datetime.date.today() + datetime.timedelta(days=7),
    )
    return resp


@app.route("/cookie2")
def cookie2():
    resp = make_response({"result": "ok"})
    resp.set_cookie(
        key="hello",
        value="world",
        expires=datetime.date.today() + datetime.timedelta(days=7),
    )
    resp.set_cookie(
        key="hi",
        value="aljun",
        expires=datetime.date.today() + datetime.timedelta(days=7),
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


@app.route("/threading")
def thread_info():
    thread_data = {}
    for thread in threading.enumerate():
        thread_data[thread.name] = {
            "threading_id": thread.ident,
            "is_alive": thread.is_alive(),
            "is_daemon": thread.isDaemon(),
            "is_current": threading.current_thread() == thread,
            "is_main": threading.main_thread() == thread,
            "is_native": thread.is_alive() and thread.isDaemon(),
            "name": thread.name,
            "native_id": thread.native_id,
        }
    return thread_data


@app.route("/process")
def process_info():
    process_data = {}

    from subprocess import Popen, PIPE
    process = Popen(['ps', '-eo' ,'pid,args'], stdout=PIPE, stderr=PIPE)
    stdout, notused = process.communicate()
    for line in stdout.splitlines():
        line = line.decode('utf-8')
        pid, cmd = line.split(' ', 1)
        process_data[pid] = cmd
    return process_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)
