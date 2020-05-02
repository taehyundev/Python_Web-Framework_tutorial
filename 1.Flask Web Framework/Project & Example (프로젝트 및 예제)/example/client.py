import requests
from datetime import datetime
import json
#
datenow =datetime.today().strftime("%Y-%m-%d")
name = input("what is your name")
response = requests.get('http://127.0.0.1:5000/api/'+name)
info = response.json()

print(info[datenow]+" contributions")

### client