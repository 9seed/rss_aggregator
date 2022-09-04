import os
import json
import opml
import feedparser
import requests
import threading
import sqlite3


class RssAggregatorService:

    def __init__(self):
        self.init_opml_file = f'/rss_aggregator_service/src/RAW.opml'
        self.outline = opml.parse(self.init_opml_file)
        self.conn = sqlite3.connect('/rss_aggregator_service/db/test.db')
        self.c = self.conn.cursor()
        self.init_table()

    def init_table(self):
        SQL = '''
        CREATE TABLE if not exists RSS 
        (
        ID TEXT PRIMARY KEY NOT NULL,
        TITLE CHAR(200) NOT NULL,
        LINK CHAR(200) NOT NULL,
        AUTHOR CHAR(50),
        UPDATED CHAR(50),
        SUMMARY TEXT,
        CONTENT TEXT
        );
        '''
        self.c.execute(SQL)
        self.conn.commit()

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
                            title = data['entries'][k].get('title', '').replace("'", '')
                            _id = data['entries'][k].get('id', '').replace("'", '')
                            link = data['entries'][k].get('link', '').replace("'", '')
                            author = data['entries'][k].get('author', '').replace("'", '')
                            updated = data['entries'][k].get('updated', '').replace("'", '')
                            summary = data['entries'][k].get('summary', '').replace("'", '')
                            try:
                                content = data['entries'][k].get('content', '')[0].value.replace("'", '')
                            except:
                                content = data['entries'][k].get('content', '').replace("'", '')
                            SQL = f'''
                            INSERT OR IGNORE INTO RSS
                            (ID, TITLE, LINK, AUTHOR, UPDATED, SUMMARY, CONTENT) 
                            VALUES ('{_id}', '{title}', '{link}', '{author}', '{updated}', '{summary}', '{content}')
                            '''
                            self.c.execute(SQL)
                            self.conn.commit()
                except Exception as e:
                    print(e)
                    continue


if __name__ == '__main__':
    cli = RssAggregatorService()
    cli.update_rss_content()