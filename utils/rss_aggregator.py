import os
import json
import opml
import feedparser
import requests
import threading


class RssAggregatorService:

    def __init__(self, init=True):
        self.init = init
        self.init_opml_file = f'/rss_aggregator_service/src/RAW.opml'
        self.outline = opml.parse(self.init_opml_file)
        self.url = 'http://0.0.0.0:8000/api/v1/rss/news/'

    def check_init(self):
        if self.init:
            for i in range(len(self.outline)):
                for j in range(len(self.outline[i])):
                    xmlUrl = self.outline[i][j].xmlUrl
                    print(xmlUrl)
                    try:
                        data = feedparser.parse(xmlUrl)
                    except Exception as e:
                        print(e)
                        continue
                    if data['entries']:
                        print(data['entries'][0].title)
                        params = {
                            'title': data['entries'][0].get('title', ''),
                            'id': data['entries'][0].get('id', ''),
                            'link': data['entries'][0].get('link', ''),
                            'author': data['entries'][0].get('author', ''),
                            'updated': data['entries'][0].get('updated', ''),
                            'summary': data['entries'][0].get('summary', ''),
                            'content': data['entries'][0].get('content', '')[0].value,
                        }
                        r = requests.post(url=self.url, json=params)
                        print(f'code: {r.status_code}, content: {r.content}')


if __name__ == '__main__':
    cli = RssAggregatorService()
    cli.check_init()