# Use an official Ubuntu Linux image as the base
FROM ubuntu:22.04

ARG USER_NAME
ARG USER_ID
ARG GROUP_ID

#setup user to host user id and groupid
RUN if [ ${USER_ID:-0} -ne 0 ] && [ ${GROUP_ID:-0} -ne 0 ]; then \
    if id $USER_NAME >/dev/null 2>&1; then userdel -f $USER_NAME; fi &&\
    if getent group $USER_NAME ; then groupdel $USER_NAME; fi &&\
    groupadd -g ${GROUP_ID} $USER_NAME &&\
    useradd -l -u ${USER_ID} -g $USER_NAME $USER_NAME &&\
    install -d -m 0755 -o $USER_NAME -g $USER_NAME /home/$USER_NAME \
;fi

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
    && apt-get install -y \
        autoconf \
        automake \
        build-essential \
        git \
        ca-certificates \
        gpg \
        wget \
        unzip \
        python3.10 \
        python3.10-dev \
        python3-pip

COPY requirements.txt ./
RUN /usr/bin/python3 -m pip install -U pip
RUN /usr/bin/python3 -m pip install --no-cache-dir -r requirements.txt

RUN chown -R $USER_NAME:$USER_NAME /home/$USER_NAME/

USER $USER_NAME
WORKDIR /home/$USER_NAME/autogen/
ENTRYPOINT /bin/bash
