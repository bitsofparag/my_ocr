# Base Image definition
# detailed reference for multi stage build Docker files
# visit: https://blog.alexellis.io/mutli-stage-docker-builds/
FROM tesseractshadow/tesseract4re:latest

ENV BASH_ENV="/root/.bashrc"
ENV LANG=en_US.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y locales locales-all \
  && echo "$LANG UTF-8" | tee /etc/locale.gen \
  && locale-gen $LANG \
  && update-locale LANG=$LANG LC_CTYPE=$LANG

RUN apt-get update \
  && apt-get install -y \
    software-properties-common \
    ca-certificates \
    build-essential \
    iputils-ping \
    curl wget \
    iptables \
    psmisc \
    libpq-dev postgresql-client \
    python3-pip \
    python3-venv \
    zip unzip \
    openssh-client \
    git \
    tzdata

RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
  && dpkg-reconfigure --frontend noninteractive tzdata

RUN echo "alias python=python3" >> ~/.bashrc
RUN echo "alias pip=pip3" >> ~/.bashrc

RUN mkdir -p /usr/src/my_ocr

COPY $PWD /usr/src/my_ocr

WORKDIR /usr/src/my_ocr

RUN pip3 install -r requirements.txt
