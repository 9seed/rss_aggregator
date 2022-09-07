import os
import json
import time

import opml
import feedparser

import requests
import threading
from pymysql.converters import escape_string
from utils.init_mysqldb import MysqlCli


class RssAggregatorService:

    def __init__(self):
        self.init_opml_file = f'/rss_aggregator_service/src/RAW.opml'
        self.outline = opml.parse(self.init_opml_file)
        self.mysql_cli = MysqlCli()

    def update_rss_content(self):
        for i in range(len(self.outline)):
            for j in range(len(self.outline[i])):
                try:
                    xmlUrl = self.outline[i][j].xmlUrl
                    print(xmlUrl)
                    data = feedparser.parse(xmlUrl)
                    if data['entries']:
                        for k in range(len(data['entries'])):
                            print(data['entries'][k].title)
                            print(time.time())
                            title = escape_string(data['entries'][k].get('title', '-'))
                            _id = escape_string(data['entries'][k].get('id', '-'))
                            link = escape_string(data['entries'][k].get('link', '-'))
                            author = escape_string(data['entries'][k].get('author', '-'))
                            updated = escape_string(data['entries'][k].get('updated', '-'))
                            summary = escape_string(data['entries'][k].get('summary', '-'))
                            try:
                                content = escape_string(data['entries'][k].get('content', '-')[0].value)
                            except:
                                content = escape_string(data['entries'][k].get('content', '-'))
                            data = {
                                '_id': _id,
                                'title': title,
                                'link': link,
                                'author': author,
                                'updated': updated,
                                'summary': summary,
                                'content': content,
                                'ts': int(time.time())
                            }
                            self.mysql_cli.upsert(data)
                except Exception as e:
                    print(e)
                    continue


if __name__ == '__main__':
    cli = RssAggregatorService()
    cli.update_rss_content()