FROM hivesolutions/python:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV HOST 0.0.0.0
ENV PORT 8080

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN pip3 install -r /requirements.txt && pip3 install -r /extra.txt && pip3 install --upgrade netius

CMD ["/usr/bin/python3", "/src/crossline/main.py"]
