from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return "Coming from server 1"


if __name__ == '__main__':
    app.run()
