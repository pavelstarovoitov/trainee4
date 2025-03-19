from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import psutil

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route('/cpu_load')
def index():
    cpu = psutil.cpu_percent()
    return f"{cpu}%"


@app.route('/flask')
def render():
    return render_template('index.html')


if __name__ == '__main__':
    print((app.name))
    app.run(debug=True)
