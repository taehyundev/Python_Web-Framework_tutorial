from flask import Flask, render_template, jsonify, make_response, request
from modules  import crawling
from urllib.request import urlopen
import urllib.parse
import json

app = Flask(__name__)

@app.route('/')
def mainpage():
    return '/'

@app.route('/api/<name>')
def getdata(name):
    print(name)
    crawling.commitCheck(name)
    with open('templates/commitdata.json', 'r',encoding='utf-8') as f:
        info = json.load(f)
        print(info)
    data = json.dumps(info,indent='\t', ensure_ascii='False')
    return data

if __name__ == "__main__":
    app.run()