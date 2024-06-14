# docker build -t aws_quiz:0.1 --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy . 

FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Asia/Tokyo

RUN apt -y update && apt -y upgrade && \
        apt install -y --no-install-recommends \
        libgl1-mesa-dev \
        libgtk2.0-dev \
        gcc \
        python3-dev \
        python3-numpy \
        python3-pip \
        wget \
        unzip && \
        apt -y clean && \
    rm -rf /var/lib/apt/lists/*

# Install python packages
RUN cd /opt && \
    pip3 install opencv-python pillow --break-system-packages

COPY main.py /opt/main.py
COPY /images/png-512.zip /opt/images/png-512.zip
COPY /dicts /opt/dicts

# unzip
RUN cd /opt/images && \
    unzip png-512.zip && \
    rm png-512.zip

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

# auth for execution
WORKDIR /opt
RUN chmod +x /opt/main.py
