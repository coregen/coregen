FROM python:3.6-alpine

RUN apk add git
RUN git clone https://github.com/coregen/coregen /var/coregen
RUN pip install /var/coregen
