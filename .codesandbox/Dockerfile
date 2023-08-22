FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3 python3-pip pipx
RUN curl -L https://github.com/autometrics-dev/am/releases/latest/download/am-linux-x86_64 -o am
RUN chmod u+x am
RUN ./am start :5000