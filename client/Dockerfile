FROM python:3.10.4-slim

RUN apt update && \
    apt install -y git && \
    rm -rf /var/lib/apt/lists/*

ADD . ./deepfake-client

WORKDIR /deepfake-client

RUN pip install --user grpcio==1.51.1 grpcio-tools==1.51.1

ENTRYPOINT ["python", "__main__.py"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]