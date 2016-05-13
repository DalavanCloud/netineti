FROM ubuntu:16.04
MAINTAINER Dmitry Mozzherin
ENV LAST_FULL_REBUILD 2016-05-12

RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install build-essential git-core python \
    python-setuptools python-dev python-numpy python-sklearn \
    python-tornado python-nose python-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install nltk
RUN python -c "import nltk; nltk.download('punkt')"

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN cd /app && python setup.py deveop

CMD ["python", "/app/bin/neti_server"]
