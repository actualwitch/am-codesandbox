FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /project

RUN apt update && apt install -y python3 python3-pip curl
RUN pip install quart autometrics==0.9
RUN curl -L https://github.com/autometrics-dev/am/releases/latest/download/am-linux-x86_64 -o am
RUN chmod u+x am
# RUN ./am start :5000