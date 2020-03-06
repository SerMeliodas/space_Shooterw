import requests
import json

class Api():
    def __init__(self):
        self.http = 'http://35.228.183.230/api/'

    def save(self,content):
        self.data = content
        url = self.http + 'save/' + content
        print(url)
        data = requests.get(url).text

        return json.loads(data)

    def get_last_news(self):
        url = self.http + 'last_news/'
        content = requests.get(url).text

        return json.loads(content)

    def get_all_news(self):
        url = self.http + 'all_news/'
        content = requests.get(url).text

        return json.loads(content)
