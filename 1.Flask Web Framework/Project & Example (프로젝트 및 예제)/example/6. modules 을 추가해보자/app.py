from flask import Flask, render_template, jsonify, make_response, request
from modules  import crawling
from urllib.request import urlopen
import urllib.parse
import json

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def getdata():
    gitID = request.form["name"]
    crawling.commitCheck(gitID)
    with open('templates/commitdata.json', 'r',encoding='utf-8') as f:
        info = json.load(f)
        print(info)
    return  json.dumps(info,indent='\t', ensure_ascii='False')

if __name__ == "__main__":
    app.run()