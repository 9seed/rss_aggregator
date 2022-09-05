RSS AGGREGATOR
====

# INTRO
This is a timed task update project to update rss messages every hour.
In main.py, schedule module to make a timed task.
In rss_aggregator, read rss xmlUrl from opml file and get the messages by using feedparser.

# HOW TO UPDATE RSS SOURCES

- check the file in ./src/RAW.opml
- add new rss source in the file with schema
```
<outline text="0x Blog - Medium" title="0x Blog - Medium" description="" type="rss" version="RSS" htmlUrl="https://blog.0xproject.com?source=rss----86e37ca8e375---4/" xmlUrl="https://blog.0xproject.com/feed"/>
```

# RUN
```
# build docker image
docker build -t rss_update:v1.0.0 .

# run docker
docker run --restart=always -d rss_update:v1.0.0
```

# HOW TO CHECK DATA

- get in to container
- connect sqlite3 db in ./db/test.db with sqlite3 driver
- write query SQL and execute