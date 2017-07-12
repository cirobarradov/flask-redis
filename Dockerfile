FROM bitnami/minideb:jessie

MAINTAINER rbravo@datiobd.com

# copy the contents of the `lib/` folder into the container at build time
ADD lib/ /lib/
# copy the contents of the `app/` folder into the container at build time
ADD app/ /app/

#run commands:
RUN apt-get update && apt-get install -y python3 python-dev python3-dev python-pip \
    && pip install virtualenv \
    # create a virtualenv we can later use
    && mkdir -p /venv/ \
    # install python version on virtual environment
    && virtualenv -p /usr/bin/python2.7 /venv \
    #activate virtual environment
    &&  /bin/bash -c "source /venv/bin/activate" \
    # install python dependencies into venv
    && /venv/bin/pip install -r /pymesos/requirements.txt --upgrade \
    # clean cache
    && apt-get clean -y  \
    && apt-get autoclean -y  \
    && apt-get autoremove -y  \

    && rm -rf /usr/share/locale/*  \
    && rm -rf /var/cache/debconf/*-old  \
    && rm -rf /var/lib/apt/lists/*  \
    && rm -rf /usr/share/doc/*

RUN chmod a+x /app/publisher.sh

ENV REDIS_SERVER redis.marathon.l4lb.thisdcos.directory
ENV CHANNEL jobs

# CMD source /venv/bin/activate
