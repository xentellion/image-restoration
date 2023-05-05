FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

ENV MKL_SERVICE_FORCE_INTEL=1

RUN apt update && \
    apt install -y \ 
        git \
        wget \
        unzip \
        libjpeg9 \
        ffmpeg \
        libsm6 \
        libxext6

WORKDIR /
RUN git clone --recurse-submodules https://github.com/Time-Travel-Rephotography/Time-Travel-Rephotography.github.io.git
WORKDIR /Time-Travel-Rephotography.github.io

RUN pip install huggingface_hub
RUN set -exo && mkdir -p checkpoint && mkdir -p checkpoint/encoder && mkdir -p third_party/face_parsing/res/cp

RUN pip install grpcio==1.51.1 grpcio-tools==1.51.1 requests==2.25.1
RUN pip install -r requirements.txt

ADD . ./
RUN python download.py 

ENTRYPOINT ["tail", "-f", "/dev/null"]

#python -m tools.data.align_images ./input ./temp
#./scripts/run.sh g ./input/origin.png 0.75