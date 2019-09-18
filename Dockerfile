FROM python:3
RUN pip install coregen

ENTRYPOINT [ "python" ]
