FROM python:3
MAINTAINER "Niraj Tolia"

WORKDIR /usr/src/busylight

RUN pip install setuptools wheel tox
RUN cd /usr/src && git clone https://github.com/LaggAt/python-govee-api.git \
       && cd python-govee-api && git checkout tags/0.2.2 && pip install .
