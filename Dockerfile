FROM ubuntu:16.04
MAINTAINER Dmitry Mozzherin
ENV LAST_FULL_REBUILD 2016-05-12

RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install build-essential git-core python3 \
    python3-setuptools python3-dev python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    pip install --upgrade pip


RUN pip3 install nltk numpy scipy scikit-learn tornado pylint nose
RUN python3 -c "import nltk; nltk.download('punkt')"

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN cd /app && python setup.py develop

CMD ["/usr/bin/python3", "/app/bin/neti_server"]
