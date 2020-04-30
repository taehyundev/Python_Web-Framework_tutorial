from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return "This is main page"

@app.route('/input')
def inputData():
    return render_template('inputdata.html')


# POST 요청
@app.route('/data', methods =['POST'])
def data():
    result = request.form
    return render_template('outputdata.html', name = result)

if __name__ == "__main__":
    app.run()