from flask import Flask,make_response, render_template,Response
app = Flask(__name__)

@app.route('/')
def main():
    return '/'

@app.route('/get_json')
def shops():
    response = make_response(render_template('shops.json'))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response
    


if __name__ == "__main__":
    app.run()