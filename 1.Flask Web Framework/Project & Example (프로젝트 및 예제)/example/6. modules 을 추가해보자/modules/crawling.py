from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup
import json
def commitCheck(name):
    timeNow = datetime.today().year
    data = dict()
    print("Hekllo")
    response = urlopen('https://github.com/'+name)
    soup = BeautifulSoup(response, 'html.parser')
    for i in soup.find_all(class_='day'):
        year = i["data-date"][0:4]
        if int(year) == int(timeNow):
            data[i["data-date"]] = i["data-count"]
            
    with open('templates/commitdata.json', 'w', encoding='utf-8') as f :
        json.dump(data, f,indent='\t',ensure_ascii=False)