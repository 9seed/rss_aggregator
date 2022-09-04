FROM python:3.8-slim
LABEL maintainer="Jarseed"

ENV PATH /usr/local/bin:$PATH

ADD . /rss_aggregator_service

WORKDIR /rss_aggregator_service

RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]
ENTRYPOINT [ "python3", "-u", "main.py"]