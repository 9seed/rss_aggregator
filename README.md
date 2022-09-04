rss_aggregator
====

RUN
===
```
# build docker image
docker build -t rss_update:v1.0.0 .

# run docker
docker run --restart=always -d rss_update:v1.0.0
```
