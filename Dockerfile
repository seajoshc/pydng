FROM python:3.6-alpine3.8

RUN pip install pydng

ENTRYPOINT [ "pydng" ]
