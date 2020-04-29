from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return '/'

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/program/<name>')
def program(name):
    return render_template('program.html', name=name)


if __name__ == "__main__":
    app.run()