# syntax = docker/dockerfile:1.3-labs
# comand: docker buildx build -t syaml .
FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y tzdata software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update

RUN apt-get install -y python2.7
RUN apt-get install -y python3.3
RUN apt-get install -y python3.4
RUN apt-get install -y python3.5
RUN apt-get install -y python3.6
RUN apt-get install -y python3.7
RUN apt-get install -y python3.8
RUN apt-get install -y python3.9 python3.9-distutils
RUN apt-get install -y python3.10 python3.10-distutils

RUN apt-get install -y python3-pip
RUN pip3 install tox

RUN mkdir -p /app
WORKDIR /app
COPY tox.ini /app
COPY pyproject.toml /app
