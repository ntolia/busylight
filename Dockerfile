FROM python:3
MAINTAINER "Niraj Tolia"

WORKDIR /usr/src/busylight


RUN pip install setuptools wheel tox O365 zoomus && apt-get -y update \
    && apt-get -y install emacs && apt-get autoclean
RUN cd /usr/src && git clone https://github.com/LaggAt/python-govee-api.git \
       && cd python-govee-api && git checkout tags/0.2.2 && pip install .
