from flask import Flask, request, url_for, redirect
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!</br>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name="Matt"):
    ip = request.remote_addr
    return render_template('hello.html', name=name, user_ip=ip)

if __name__ == "__main__":
    app.run()