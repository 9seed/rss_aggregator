import os
import opml
import feedparser
from moduls.pg_init import PGCli


class RssAggregatorService:

    def __init__(self, init=True):
        self.init = init
        self.init_opml_file = f'/rss_aggregator_service/src/RAW.opml'
        self.outline = opml.parse(self.init_opml_file)
        # self.pgcli = PGCli()

    def check_init(self):
        if self.init:
            for i in range(len(self.outline)):
                for j in range(len(self.outline[i])):
                    xmlUrl = self.outline[i][j].xmlUrl
                    data = feedparser.parse(xmlUrl)
                    print(data['entries'][0].title)
                    # for n in range(len(data['entries'])):
                    #     print(data['entries'][n])
                        # self.pgcli.update_news(data['entries'][n])

    def update_from_src(self):
        for i in range(len(self.outline)):
            for j in range(len(self.outline[i])):
                xmlUrl = self.outline[i][j].xmlUrl
                data = feedparser.parse(xmlUrl)
                print(data['entries'][0].title)
                # for n in range(len(data['entries'])):
                #     print(data['entries'][n])
                    # self.pgcli.update_news(data['entries'][n])
