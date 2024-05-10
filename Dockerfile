# Use an official Ubuntu Linux image as the base
FROM ubuntu:22.04

ARG USER_NAME
ARG USER_ID
ARG GROUP_ID

ARG PYTHON_VERSION=3.10
ARG NODE_MAJOR=20

#setup user to host user id and groupid
RUN if [ ${USER_ID:-0} -ne 0 ] && [ ${GROUP_ID:-0} -ne 0 ]; then \
    if id $USER_NAME >/dev/null 2>&1; then userdel -f $USER_NAME; fi &&\
    if getent group $USER_NAME ; then groupdel $USER_NAME; fi &&\
    groupadd -g ${GROUP_ID} $USER_NAME &&\
    useradd -l -u ${USER_ID} -g $USER_NAME $USER_NAME &&\
    install -d -m 0755 -o $USER_NAME -g $USER_NAME /home/$USER_NAME \
;fi

RUN echo 'root:toor' | chpasswd

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y ca-certificates curl gpg
RUN apt-get update \
    && apt-get upgrade -y  \
    && apt-get -y install --no-install-recommends \
        autoconf \
        automake \
        build-essential \
        git \
        git-lfs \
        wget \
        unzip \
        xz-utils \
        rsync \
        libglu1-mesa \
        ${PYTHON_VERSION} \
        ${PYTHON_VERSION}-dev \
        python3-pip \
   && apt-get autoremove -y \
   && apt-get clean -y \
   && arch=$(arch | sed s/aarch64/arm64/ | sed s/x86_64/amd64/) \
   && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.5.23/quarto-1.5.23-linux-${arch}.deb \
   && dpkg -i quarto-1.5.23-linux-${arch}.deb \
   && rm -rf /var/lib/apt/lists/* quarto-1.5.23-linux-${arch}.deb

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

#clean up apt files, reduce docker size
RUN rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python${PYTHON_VERSION} 1 \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 1 \
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

#ENV FLUTTER_HOME=/home/$USER_NAME/tools/flutter
#ENV PATH="$PATH:$FLUTTER_HOME/bin"

## Install Flutter SDK
#RUN git clone https://github.com/flutter/flutter.git $FLUTTER_HOME
## Pre-download Flutter dependencies
#RUN flutter precache
## Verify Flutter installation
#RUN flutter doctor
#
#RUN npm install -g gatsby-cli
#RUN npm install --global yarn
#
#COPY requirements.txt ./
RUN /usr/bin/python${PYTHON_VERSION} -m pip install -U pip
#RUN /usr/bin/python${PYTHON_VERSION} -m pip install --no-cache-dir -r requirements.txt

#RUN npm install --global yarn
#RUN pip install --upgrade pip
#RUN pip install pydoc-markdown
#RUN pip install pyyaml
#RUN pip install termcolor
#RUN pip install colored
#RUN pip install nbclient
#RUN pip install nbformat
RUN pip install scikit-learn
RUN pip install autogenstudio

#ENV PATH=/home/$USER_NAME/.local/bin:$PATH
#ENV PYTHONPATH=/home/$USER_NAME/apis/AutoGPT/autogpt/autogpt:/home/$USER_NAME/apis/autogen/autogen:$PYTHONPATH

RUN chown -R $USER_NAME:$USER_NAME /home/$USER_NAME/

USER $USER_NAME
WORKDIR /home/$USER_NAME/workspace/

#EXPOSE 5000
#autogen studio
#EXPOSE 8000
#EXPOSE 8001

ENTRYPOINT /bin/bash
