FROM python:3.8-slim
LABEL maintainer="Jarseed"

ENV PATH /usr/local/bin:$PATH

ADD . /rss_aggregator_service

WORKDIR /rss_aggregator_service

RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary

CMD ["/bin/bash"]
#CMD ["python3", "main.py"]
ENTRYPOINT [ "python3", "-u", "main.py"]